from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.models import Makanan

def hapusMakanan(request):
    makanans = Makanan.getAllMakanan()
    content = {"makanans":makanans}
    return render(request, "hapusMakanan.html", content)