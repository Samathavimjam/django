from django import forms

class TaskForm(forms.Form):
    taskname=forms.CharField()
    taskcompleted=forms.BooleanField()