from django.http.response import HttpResponseRedirect
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.
def index(request):
    tasks=MyTask.objects.all()
    form=TaskForm()
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("list"))   

    context={"tasks":tasks, "form":form}
    return render(request,"tasks/list.html",context)

def update_task(request,primary_key):
   allTask= MyTask.objects.get(id=primary_key)

   form=TaskForm(instance=allTask)


   if request.method=='POST':
       form=TaskForm( request.POST, instance=allTask)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse("list"))  
   context={'form':form}
   return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):
    item=MyTask.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return HttpResponseRedirect(reverse("list"))  
    context={"item":item}
    return render(request,'tasks/delete.html')   
