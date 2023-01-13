from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from menu.models import Makanan

def menuPage(request):
    makanans = Makanan.getAllMakanan()
    content = {"makanans":makanans}
    return render(request, "menu.html", content)

def savePage(request):
    template = loader.get_template('save.html')
    return HttpResponse(template.render())

