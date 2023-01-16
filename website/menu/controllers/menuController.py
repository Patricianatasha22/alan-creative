from django.shortcuts import render, redirect
from django.http import HttpResponse
from menu.models import Makanan, Pesanan
from menu.forms import hitungKembalianForm

# TO SEND EMAIL
from django.core.mail import send_mail

# TO PRINT
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def menuPage(request):
    makanans = Makanan.getAllMakanan()
    pesanans = Pesanan.getAllPesanan()
    total = Pesanan.getTotal()

    # #hitung Kembalian Modal
    # if request.method == 'POST':
    #     print("hello")
    #     form = hitungKembalianForm(request.POST)
    #     if form.is_valid():
    #         totalCharge = form.cleaned_data.get('Total_Charge')
    #         uangPembeli = form.cleaned_data.get('Uang_Pembeli')

    #         uangKembalian = totalCharge - uangPembeli

    #         content = {"makanans":makanans , "pesanans": pesanans, "total": total, "uangKembalian": uangKembalian}
    #         return render(request, "menu.html", content)
    # else:
    form = hitungKembalianForm(initial={'Total_Charge': total})

    content = {"makanans":makanans , "pesanans": pesanans, "total": total, "form": form}
    
    return render(request, "menu.html", content)

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

def saveAndPrint(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw the HTML on the PDF
    p.drawString(20, 800, "This is Your Bill")

    # creating data
    p.drawString(20,750,'Nama')
    p.drawString(400,750,'Jumlah Pesanan')
    p.drawString(500,750,'Total Harga')

    pesanans = Pesanan.getAllPesanan()

    y = 700
    for pesanan in pesanans:
        p.drawString(20,y, pesanan.makanan.nama)
        p.drawString(400,y, str(pesanan.jumlah))
        p.drawString(500,y, str(pesanan.totalHarga))
        y-=50
    p.drawString(400,y,"Total")
    p.drawString(500,y, str(Pesanan.getTotal()))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    return response

def saveBill(request):

    if request.method == "POST":

        email = request.POST["email"]

        # creating data
        data = ""
        pesanans = Pesanan.getAllPesanan()
        for pesanan in pesanans:
            data += f"{pesanan.makanan.nama:<50} {pesanan.jumlah}x {pesanan.totalHarga:,}\n"

        send_mail('YOUR BILL',
            data,
            'nextlevelt05@gmail.com',
            [email],
            fail_silently=False)
    
    return redirect('menu')

from django.http import JsonResponse
def hitungKembalian(request):
    if request.method == 'POST':
        form_data = request.POST
        totalCharge = form_data.get('totalCharge')
        uangPembeli = form_data.get('uangPembeli')
        totalCharge = totalCharge.replace(",", "")
        uangKembalian = int(totalCharge)-int(uangPembeli)

        result = f"Uang kembalian: {uangKembalian}"
        print(result)

        return JsonResponse({'result': result})