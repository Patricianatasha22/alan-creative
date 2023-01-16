from django.urls import path
from menu.controllers import menuController, tambahMakananController, hapusMakananController, editMakananController

urlpatterns = [
    # MENU
    path('', menuController.menuPage, name = 'menu'),
    path('pesan/<int:id>/', menuController.pesan, name = 'pesan'),
    path('clearsale/', menuController.clearSale, name='clearSale'),
    path('hitungKembalian/', menuController.hitungKembalian, name='hitungKembalian'),
    path('saveBill/', menuController.saveBill, name='saveBill'),
    path('saveAndPrint/', menuController.saveAndPrint, name='saveAndPrint'),
    
    # CRUD MAKANAN
    path('tambahMakanan/', tambahMakananController.tambahMakanan, name = 'tambahMakanan'),
    path('hapusMakanan/', hapusMakananController.hapusMakanan, name = 'hapusMakanan'),
    path('pilihMakanan/', editMakananController.pilihMakanan, name="pilihMakanan"),
    path('pilihMakanan/editMakanan/<int:id>', editMakananController.editMakanan, name ='editMakanan'),

]