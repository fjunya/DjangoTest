#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    response = HttpResponse()
    response.write("<p>Here's the text of the Web page.</p>")
    return response