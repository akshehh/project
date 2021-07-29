from django.shortcuts import redirect, render
from django.contrib import admin
from django.http import HttpResponse
from .models import CrudOperation
from .forms import CrudForm

# Create your views here.
def get(request):
    form = CrudForm()
    data = CrudOperation.objects.all()
    return render(request,'index.html',{'form':form,'data':data})

def getId(request,id):
    data = CrudOperation.objects.get(id=id)
    form = CrudForm(instance=data)
    return render(request,'edit.html',{'form':form,'data':data})

def post(request):
    form = CrudForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(get)

def display(request):
    data=CrudOperation.objects.all()
    return render(request,'display.html',{'data':data})



def update(request,id):
    print(id)
    data = CrudOperation.objects.get(id=id)
    form = CrudForm(request.POST,instance=data)
    if(form.is_valid()):
        form.save()
    return redirect(display)



def delete(request,id):
    data = CrudOperation.objects.get(id=id)
    data.delete()
    return redirect(display)


