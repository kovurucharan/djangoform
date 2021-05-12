from django.shortcuts import render,redirect
from WebApp.forms import EmployeeForm
from WebApp.models import Employee
# Create your views here.
from django.http import HttpResponseRedirect
from WebApp import forms
def Thanks(request):
    return render(request,'MyApp/thanks.html')

def Register(request):
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thank/')
    else:
        form=forms.EmployeeForm()
    return render(request,'MyApp/register.html',{'form':form})