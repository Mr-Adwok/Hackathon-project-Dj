from django.db import models
from courses.models import Course
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    obtain_marks = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

  