# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def stu(request):
    if request.method=='POST':
        form = Student_info(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass

    else:
        form = Student_info()
    return render(request,'index.html',{'form':form})
