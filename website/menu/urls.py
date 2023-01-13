from django.urls import path
from menu.controllers import menuController, tambahMakananController, hapusMakananController

urlpatterns = [
    path('', menuController.menuPage, name = 'menu'),
    path('save/', menuController.savePage, name = 'savePage'),
    path('tambahMakanan/', tambahMakananController.tambahMakanan, name = 'tambahMakanan'),
    path('hapusMakanan/', hapusMakananController.hapusMakanan, name = 'hapusMakanan')
]