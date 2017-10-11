from django.db import models

__all__ = (
    'School',
    'CommonInfo',
    'Student',
    'Teacher',
)


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    school = models.ForeignKey(School, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)
