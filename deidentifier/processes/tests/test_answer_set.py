from django.test import TestCase
from django.urls import reverse

from processes.models import AnswerSet, Answer


class AnswerSetTest(TestCase):
    fixtures = ['question_group_1.json']

    def setUp(self):
        AnswerSet.objects.create(title="Test Answer Set", description="This is an answers set for testing.")

    def test_redirect_to_first_question_page_on_successful_answer_set_creation(self):
        AnswerSet.objects.create(title="Test Answer Set", description="This is an answers set for testing.")
        response = self.client.post(reverse("create"), {"title": "Test Title", "description": "Test Description"})
        self.assertRedirects(response, "/processes/3/page/1/")

    def test_answer_created_on_answer_set_creation(self):
        answer_set = AnswerSet.objects.get(title="Test Answer Set")
        answers = Answer.objects.filter(answer_set=answer_set)
        self.assertEqual(answers.__len__(), 6)

    def test_answers_do_not_duplicate_on_update(self):
        answer_set = AnswerSet.objects.get(title="Test Answer Set")
        answer_set.save()
        answers = Answer.objects.filter(answer_set=answer_set)
        self.assertEqual(answers.__len__(), 6)
