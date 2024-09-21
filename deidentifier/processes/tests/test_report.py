from django.test import TestCase
from django.urls import reverse

from processes.models import AnswerSet


class ReportTest(TestCase):
    fixtures = ['question_group_1.json', 'question_group_2.json', 'question_group_3.json']

    def test_report_redirects_to_last_question_if_insufficient_information(self):
        AnswerSet.objects.create(title="Test Answer Set", description="This is an answers set for testing.")
        response = self.client.get(reverse("report", kwargs={'answer_set_id': 1}))
        self.assertRedirects(response, "/processes/1/page/3/")
