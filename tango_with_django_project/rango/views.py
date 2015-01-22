from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello yet again!")
def about(request):
    return HttpResponse("This tutorial has been put together by Stig Rasmus Renvall, 2089278")