from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def sayHelloWorld(request):
    text = """<h1>Hello ,Welcome to Django World</h1>"""
    return HttpResponse(text)
