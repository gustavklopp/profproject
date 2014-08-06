import os

from django.db import models
from django.contrib.auth.models import User


class Discipline(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    discipline = models.ForeignKey(Discipline)
    exo_number = models.IntegerField()
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=30)
    question_date = models.DateField()
    file = models.FileField(upload_to='static/exercises')

    def __str__(self):
        return "{0} / {1!s}".format(self.discipline, self.exo_number)

""" classes containing the result. Exoresult: with the total score for one exercise,
                                   Exoresultdetail: score (bool) for each question inside exercise."""


class Exo(models.Model):
    user = models.ForeignKey(User)
    discipline = models.ForeignKey(Discipline, null=True)
    exo_number = models.IntegerField()
    result_date = models.DateTimeField(null=True)
    try_number = models.IntegerField(default='1')

    def __str__(self):
        return "{0} / {1!s} / {2}".format(self.discipline, self.exo_number, self.user)

    class Meta:
        abstract = True


class ExoResult(Exo):
    result = models.IntegerField()


class ExoResultDetail(Exo):
    truth = models.BooleanField(default=False)
    exo_number_detail = models.IntegerField(default=0)

    def __str__(self):
        return "{0}/{1!s}/{2!s}/{3}".format(self.discipline, self.exo_number, self.exo_number_detail, self.user)
