from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    cat_one = models.IntegerField()
    cat_two = models.IntegerField()
    fat = models.IntegerField()
    total = models.IntegerField()

 