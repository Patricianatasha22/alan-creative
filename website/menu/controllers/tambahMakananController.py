from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.forms import tambahMakananForm 

def tambahMakanan(request):
    if request.method == 'POST':
        form = tambahMakananForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('menu')
        
    else:
        form = tambahMakananForm()
    
    return render(request, "tambahMakanan.html", {"form": form})
