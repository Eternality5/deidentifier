from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

ANSWER_FORMATS = [
    ("boolean", "boolean"),
    ("integer", "integer"),
    ("string", "string"),
    ("list", "list"),
]


class QuestionGroup(models.Model):
    sequence_number = models.IntegerField(default=None)
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    help_tip = models.TextField(default=None)
    source = models.CharField(max_length=2_083, default=None)  # maximum chrome url length


class Question(models.Model):
    question_group_id = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    sequence_number = models.IntegerField(default=None)
    question = models.TextField(default=None)
    help_tip = models.TextField(default=None)
    is_compulsory = models.BooleanField(default=None)
    answer_format = models.CharField(max_length=255, default=None, choices=ANSWER_FORMATS)


class AnswerSet(models.Model):
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)


class Answer(models.Model):
    answer_set = models.ForeignKey(AnswerSet, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    int_answer = models.PositiveIntegerField(default=None, blank=True, null=True)
    string_answer = models.TextField(default=None, blank=True, null=True)
    boolean_answer = models.BooleanField(default=None, blank=True, null=True)
    multiple_answer = models.TextField(default=None, blank=True, null=True)

    @classmethod
    def create(cls, answer_set, question_id):
        answer = cls(answer_set=answer_set, question_id=question_id)
        return answer


# method for updating
@receiver(post_save, sender=AnswerSet, dispatch_uid="create_answer_instances")
def build_answers(sender, instance, **kwargs):
    if not kwargs["raw"]:
        questions = Question.objects.all()
        # This prevents answers being regenerated on update
        if Answer.objects.filter(answer_set=instance).__len__() == 0:
            for question in questions:
                answer = Answer.create(instance, question)
                answer.save()
