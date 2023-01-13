from django.urls import path
from menu.controllers import menuController, tambahMakananController, hapusMakananController

urlpatterns = [
    path('', menuController.menuPage, name = 'menu'),
    path('pesan/<int:id>/', menuController.pesan, name = 'pesan'),
    path('clearsale/', menuController.clearSale, name='clearSale'),
    path('save/', menuController.savePage, name = 'savePage'),
    path('tambahMakanan/', tambahMakananController.tambahMakanan, name = 'tambahMakanan'),

    path('hapusMakanan/', hapusMakananController.hapusMakanan, name = 'hapusMakanan')
]