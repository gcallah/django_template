from django.contrib.auth.models import User
from django.db import models


QUEST_LEN = 256
ANS_LEN = 128
MODNM_LEN = 16
DEF_PASS = 80.0

QTYPES = (
    ("MCHOICE", "Multiple choice"),
    ("TF", "True/False"),
    ("BLANK", "Fill-in-the-blank"),
    ("ESSAY", "Essay"),
)


class Question(models.Model):
    text = models.CharField(max_length=QUEST_LEN)
    difficulty = models.IntegerField(null=True, blank=True)
    qtype = models.CharField(choices=QTYPES, max_length=10)
    correct = models.CharField(max_length=1)
    answerA = models.CharField(max_length=ANS_LEN, null=True, blank=True)
    answerB = models.CharField(max_length=ANS_LEN, null=True, blank=True)
    answerC = models.CharField(max_length=ANS_LEN, null=True, blank=True)
    answerD = models.CharField(max_length=ANS_LEN, null=True, blank=True)
    answerE = models.CharField(max_length=ANS_LEN, null=True, blank=True)

    def __str__(self):
        return self.text
