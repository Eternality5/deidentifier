from django.test import TestCase
from django.urls import reverse


class QuestionGroupViewTest(TestCase):
    fixtures = ['all_question_types.json']

    def test_question_group_page_renders(self):
        response = self.client.get(reverse("question", kwargs={'answer_set_id': 1, 'question_group_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_boolean_questions_display_initial_value(self):
        response = self.client.get(reverse("question", kwargs={'answer_set_id': 1, 'question_group_id': 1}))
        self.assertContains(response, 'true')

    def test_integer_answers_display_initial_value(self):
        response = self.client.get(reverse("question", kwargs={'answer_set_id': 1, 'question_group_id': 1}))
        self.assertContains(response, '1')
