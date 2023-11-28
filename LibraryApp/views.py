from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone


def index(request):
    context = {"message" : "Ma bibliothèque"}
    template = loader.get_template("LibraryApp/index.html")
    return HttpResponse(template.render(context,request))
   