from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def checkoutPage(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())

def savePage(request):
    template = loader.get_template('save.html')
    return HttpResponse(template.render())