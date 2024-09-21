import logging

from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from processes.models import Answer, AnswerSet, Question, QuestionGroup
from processes.views import render_with_htmx

logger = logging.getLogger(__name__)


def remove_unnecessary_questions(answer_set, questions, answers):
    """
    Removes question that are non needed, for example K-Map question aren't relevant if there is a persecutor risk

    param answer_set: the answer_set that to reference previous answers from, so it knows what to exclude
    param questions: the current set of questions to be rendered onto the page
    param answers: the current set of answers to the question to be rendered onto the page
    return: returns the (questions, answers) with the unnecessary questions and answers removed
    """
    excluded_questions = []
    persecutor_questions = Answer.objects.filter(answer_set=answer_set, question_id__in=[201, 202, 203])

    if Answer.objects.filter(answer_set=answer_set, question_id=301):
        is_subset = Answer.objects.filter(answer_set=answer_set, question_id=301)[0].boolean_answer
    else:
        is_subset = False

    persecutor_risk = is_subset is False or is_subset is None
    for persecutor_question in persecutor_questions:
        persecutor_risk = (persecutor_question.boolean_answer
                           or persecutor_risk
                           or persecutor_question.boolean_answer is None)

    if persecutor_risk:
        excluded_questions.append(303)
    else:
        excluded_questions.append(302)

    questions = questions.exclude(pk__in=excluded_questions)
    answers = answers.exclude(question_id__in=excluded_questions)
    return questions, answers


def get_navigation_buttons(answer_set_id, question_group_id):
    """
    gets the urls to the previous and next page in the question survey

    param answer_set_id: the id of the answer set needed to create the destination url
    param question_group_id: the id of the question group
    return: (previous_page_number, next_page_number), an array of urls to navigate to
    """
    next_page_number = (reverse('question', args=[answer_set_id, question_group_id + 1])
                        if question_group_id < QuestionGroup.objects.all().__len__() else
                        reverse('report', args=[answer_set_id]))

    previous_page_number = (reverse('question', args=[answer_set_id, question_group_id - 1])
                            if question_group_id > 1 else
                            reverse('update', args=[answer_set_id]))
    return previous_page_number, next_page_number


def question(request, answer_set_id, question_group_id):
    """
    used to return a page where a user can answer a group of questions

    param request: WSGIRequest
    param answer_set_id: id of the answer_set to pre-populate and store the question in
    param question_group_id: id of the question group to display (at the time of writing there are only 3)
    return: A page displaying the specified question group prepopulated from the answers in the answer_set specified
    """
    answer_form_set = modelformset_factory(Answer,
                                           fields=['int_answer', 'boolean_answer', 'string_answer', 'multiple_answer'])

    answer_set = get_object_or_404(AnswerSet, id=answer_set_id)
    question_group = get_object_or_404(QuestionGroup, id=question_group_id)

    questions = Question.objects.filter(question_group_id=question_group)
    answers = Answer.objects.filter(answer_set=answer_set, question_id__in=questions.all())

    questions, answers = remove_unnecessary_questions(answer_set, questions, answers)
    previous_page_number, next_page_number = get_navigation_buttons(answer_set_id, question_group_id)

    formset = answer_form_set(request.POST or None, queryset=answers)
    if request.method == "POST":
        if formset.is_valid():
            formset.save()
            if question_group_id >= QuestionGroup.objects.all().__len__():
                return HttpResponseRedirect(reverse('report', args=[answer_set_id]))
            else:
                return HttpResponseRedirect(reverse('question', args=[answer_set_id, question_group_id + 1]))
        else:
            logger.error(formset.errors)

    # Packaging question and answer so they can be iterated through
    question_answer_pairs = zip(questions, formset)
    context = {
        "question_answer_pairs": question_answer_pairs,
        "question_group": question_group,
        "formset": formset,
        "next_page_number": next_page_number,
        "previous_page_number": previous_page_number,
    }

    return render_with_htmx(request, "question_group_page.html", context)
