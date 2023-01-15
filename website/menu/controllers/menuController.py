from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.models import Makanan, Pesanan
from menu.forms import hitungKembalianForm

def menuPage(request):
    makanans = Makanan.getAllMakanan()
    pesanans = Pesanan.getAllPesanan()
    total = Pesanan.getTotal()

    #hitung Kembalian Modal
    if request.method == 'POST':
        print("hello")
        form = hitungKembalianForm(request.POST)
        if form.is_valid():
            totalCharge = form.cleaned_data.get('Total_Charge')
            uangPembeli = form.cleaned_data.get('Uang_Pembeli')

            uangKembalian = totalCharge - uangPembeli

            content = {"makanans":makanans , "pesanans": pesanans, "total": total, "uangKembalian": uangKembalian}
            return render(request, "menu.html", content)
    else:
        form = hitungKembalianForm(initial={'Total_Charge': total})

    content = {"makanans":makanans , "pesanans": pesanans, "total": total, "form": form}
    
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