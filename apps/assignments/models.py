from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    obtain_marks = models.IntegerField()

  