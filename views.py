from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World!!!!")

def about(request):
    data = {'name':'Chanikya','age':20}
    return render(request,'index.html',data)

