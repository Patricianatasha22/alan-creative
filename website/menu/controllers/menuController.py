from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.models import Makanan, Pesanan

def menuPage(request):
    makanans = Makanan.getAllMakanan()
    pesanans = Pesanan.getAllPesanan()

    content = {"makanans":makanans , "pesanans": pesanans}
    return render(request, "menu.html", content)

def savePage(request):
    template = loader.get_template('save.html')
    return HttpResponse(template.render())

def pesan(request, id):
    makanans = Pesanan.getAllMakananUnik()
    print(makanans)
    print(id)
    if id in makanans:
        Pesanan.updateJumlah(id)
    else:
        pesanan = Pesanan.createPesanan(id)

    return redirect('menu')

def clearSale(request):
    Pesanan.clearSale()
    return redirect('menu')