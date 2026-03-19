from django.shortcuts import render,redirect

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def list(request):
    ETDLO=TaskForm()
    d={'ETDLO':ETDLO}
    if request.method=='POST':
        DTDLO=TaskForm(request.POST)
        if DTDLO.is_valid():
            tn=DTDLO.cleaned_data['taskname']
            tc=DTDLO.cleaned_data['taskcompleted']
            TO=Task.objects.get_or_create(taskname=tn,taskcompleted=tc)
            if TO[1]:
                return HttpResponse("created")
            else:
                return HttpResponse("not created")
        else:
            return HttpResponse("invalid")
    return render(request,'list.html',d)


def task(request):
    TTO=Task.objects.all()
    d={'TTO':TTO}
    return render(request,'task.html',d)


def delete(request,id):
    tdo=Task.objects.get(id=id)
    tdo.delete()
    return redirect('task')