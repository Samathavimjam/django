from django.db import models

# Create your models here.
class Task(models.Model):
    taskname=models.CharField(primary_key=True,max_length=100)
    taskcompleted=models.BooleanField()
