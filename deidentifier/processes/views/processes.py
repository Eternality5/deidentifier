from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from processes.forms import AnswerSetForm
from processes.models import AnswerSet
from processes.views.render_with_htmx_helper import render_with_htmx


def index(request):
    """
    This view renders a list of all the answers sets

    param request: WSGIRequest
    return: html page with containing a list of all answer_sets
    """
    latest_answer_set_list = AnswerSet.objects.order_by("title")
    context = {"latest_answer_set_list": latest_answer_set_list, }
    return render_with_htmx(request, "process_list.html", context)


def update(request, answer_set_id):
    """
    update() acts as both the update and details page for an answer_set

    param request: WSGIRequest
    param answer_set_id: The id of the answer set to be rendered
    return: html page containing the page to update answer_set_details
    """
    answer_set = get_object_or_404(AnswerSet, id=answer_set_id)

    if request.method == "POST":
        form = AnswerSetForm(request.POST, instance=answer_set)
        if form.is_valid():
            if form.has_changed():
                form.save()
            return HttpResponseRedirect(reverse("question",
                                                kwargs={"answer_set_id": answer_set.pk, "question_group_id": 1}))

    form = AnswerSetForm(instance=answer_set)
    context = {"process": answer_set, "form": form}
    return render_with_htmx(request, "process_details.html", context)


def delete(request, answer_set_id):
    """
    delete() deletes a given process and redirects to the index page

    param request: WSGIRequest
    param answer_set_id: The id of the answer set to be deleted
    return: redirection to the index route
    """
    process = get_object_or_404(AnswerSet, id=answer_set_id)
    process.delete()
    return redirect('index')


def create(request):
    """
    create() either creates a new answer_set or renders the page for creating a new answer_set

    param request: WSGIRequest
    return: A redirect to the answer_set page created by the POST request or GETs the answer_set creation page
    """
    form = AnswerSetForm
    if request.method == "POST":
        form = AnswerSetForm(request.POST, instance=None)
        if form.is_valid():
            answer_set = form.save()
            return HttpResponseRedirect(reverse("question",
                                                kwargs={"answer_set_id": answer_set.pk, "question_group_id": 1}))
    return render_with_htmx(request, "process_create.html", context={'form': form})
