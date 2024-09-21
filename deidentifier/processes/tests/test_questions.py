from django.test import TestCase
from django.urls import reverse

from processes.models import AnswerSet, Answer


class QuestionsTest(TestCase):
    fixtures = ['question_group_1.json', 'question_group_2.json', 'question_group_3.json']
    persecutor_risk_text = 'What is the current K-Anonymity of the dataset?'
    no_persecutor_risk_text = 'What is the K-Anonymity of the dataset when combined with the larger dataset?'

    def is_persecutor_risk_response(self, answer_set_id):
        response = self.client.get(
            reverse("question", kwargs={'answer_set_id': answer_set_id, 'question_group_id': 3}))
        self.assertContains(response, QuestionsTest.persecutor_risk_text)
        self.assertNotContains(response, QuestionsTest.no_persecutor_risk_text)

    def is_not_persecutor_risk_response(self, answer_set_id):
        response = self.client.get(
            reverse("question", kwargs={'answer_set_id': answer_set_id, 'question_group_id': 3}))
        self.assertNotContains(response, QuestionsTest.persecutor_risk_text)
        self.assertContains(response, QuestionsTest.no_persecutor_risk_text)

    def test_persecutor_risk_if_questions_unanswered(self):
        answer_set_id = 4
        AnswerSet.objects.create(pk=answer_set_id, title="Test Title", description="Test description.")
        QuestionsTest.is_persecutor_risk_response(self, answer_set_id)

    def test_persecutor_risk_if_question_unanswered_even_when_subset(self):
        answer_set_id = 5
        AnswerSet.objects.create(pk=answer_set_id, title="Test Title", description="Test description.")
        subset_question = Answer.objects.filter(answer_set=answer_set_id, question_id=301)
        subset_question[0].boolean_answer = True
        subset_question[0].save()
        QuestionsTest.is_persecutor_risk_response(self, answer_set_id)

    def test_only_k_anonymity_question_when_persecutor_risk_is_present(self):
        answer_set_id = 1
        AnswerSet.objects.create(pk=answer_set_id, title="Test Title", description="Test description.")
        persecutor_question = Answer.objects.filter(answer_set=answer_set_id, question_id=201)
        persecutor_question[0].boolean_answer = True
        persecutor_question[0].save()
        QuestionsTest.is_persecutor_risk_response(self, answer_set_id)

    def test_only_k_map_question_when_persecutor_risk_is_NOT_present(self):
        answer_set_id = 3
        AnswerSet.objects.create(pk=answer_set_id, title="Test Title", description="Test description.")
        persecutor_questions = Answer.objects.filter(answer_set=answer_set_id, question_id__in=[201, 202, 203])
        subset_questions = Answer.objects.filter(answer_set=answer_set_id, question_id=301)
        for persecutor_question in persecutor_questions:
            persecutor_question.boolean_answer = False
            persecutor_question.save()
        for subset_question in subset_questions:
            subset_question.boolean_answer = True
            subset_question.save()
        QuestionsTest.is_not_persecutor_risk_response(self, answer_set_id)
