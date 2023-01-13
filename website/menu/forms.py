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