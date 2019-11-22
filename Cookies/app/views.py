# -*- coding: utf-8 -*-
from django.http import HttpResponse  
      
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('name', 'sachin')  
    return response  
def getcookie(request):  
    result  = request.COOKIES['name']  
    return HttpResponse("info @: "+  result);  