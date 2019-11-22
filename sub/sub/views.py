from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request,'home.html',{'name':'sachin'})

def sub(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    if val1 > val2:
        result=val1 - val2
    else:
        result=val2 - val1

    return render(request,'result.html',{'results':result})