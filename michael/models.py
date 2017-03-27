from django.db import models

# Create your models here.

class Person(models.Model):
    firstName = models.TextField(default='')
    middleInitial = models.TextField(default='')
    lastName = models.TextField(default='')

class Education(models.Model):
    person = models.ForeignKey(Person, default=None)
    degree = models.TextField(default='')
    major = models.TextField(default='')
    school = models.TextField(default='')
    yearCompleted = models.TextField(default='')

    class Meta:
        ordering = ('-yearCompleted',)

class Job(models.Model):
    person = models.ForeignKey(Person, default=None)
    jobTitle = models.TextField(default='')
    employer = models.TextField(default='')
    startYear = models.TextField(default='')
    endYear = models.TextField(default='')



