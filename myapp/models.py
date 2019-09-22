from django.db import models


# Create your models here.
class Grade(models.Model):
    gid = models.IntegerField()
    name = models.CharField(max_length=30)
    add_date = models.DateTimeField()


class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=30)
    add_date = models.DateTimeField()
    sgrade = models.ForeignKey("Grade", on_delete=models.CASCADE)
