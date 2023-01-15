from django.db import models  
from django.forms import fields  
from django import forms  
from menu.models import Makanan
  
  
class tambahMakananForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Makanan 
        # It includes all the fields of model  
        fields = '__all__'  

class hitungKembalianForm(forms.Form):
    Total_Charge = forms.IntegerField()
    Uang_Pembeli = forms.IntegerField()