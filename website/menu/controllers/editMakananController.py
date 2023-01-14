from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.forms import tambahMakananForm 
from menu.models import Makanan


def pilihMakanan(request):
    makanans = Makanan.getAllMakanan()
    content = {"makanans":makanans}

    return render(request, 'pilihMakanan.html', content)

def editMakanan(request,id):
    makanan = Makanan.getMakananByID(id)

    if request.method == 'POST':
        form = tambahMakananForm(request.POST, request.FILES, instance = makanan)

       
        if form.is_valid():
            if form.cleaned_data['gambar']:
                makanan.gambar = form.cleaned_data['gambar']
            makanan.save()
            form.save()
            return redirect('menu')
        
    else:
        form = tambahMakananForm(instance = makanan)

    return render(request, 'editMakanan.html', {"form":form})
        


    