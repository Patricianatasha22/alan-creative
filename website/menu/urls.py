from django.urls import path
from menu.controllers import checkoutController

urlpatterns = [
    path('', checkoutController.checkoutPage, name = 'checkoutPage'),
    path('save/', checkoutController.savePage, name = 'savePage')
]