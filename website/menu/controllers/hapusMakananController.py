from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.models import Makanan

def hapusMakanan(request):
    if request.method == 'POST':
        makanans = request.POST.getlist('hapusMakananList')
        for makanan in makanans:
            Makanan.deleteMakanan(makanan)

        return redirect('menu')
    else:
        makanans = Makanan.getAllMakanan()
        content = {"makanans":makanans}

    return render(request, "hapusMakanan.html", content)