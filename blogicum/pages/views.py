from django.shortcuts import render

from django.http import HttpResponse

def about(response):
    template_name = "pages/about.html"
    return render(response, template_name)

def rules(response):
    template_name = "pages/rules.html"
    return render(response, template_name)
