from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:answer_set_id>/", views.update, name="update"),
    path("new/", views.create, name="create"),
    path("delete/<int:answer_set_id>/", views.delete, name="delete"),
    path("<int:answer_set_id>/page/<int:question_group_id>/", views.question, name="question"),
    path("<int:answer_set_id>/report", views.report, name="report"),
    path("<int:answer_set_id>/report/pdf", views.report_pdf, name="report_pdf")
]
