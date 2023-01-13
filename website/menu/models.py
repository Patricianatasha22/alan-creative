from django.db import models
# Create your models here.

class Makanan(models.Model):

    class meta:
        db_table = 'makanan'

    nama = models.CharField(max_length=50, default=None)
    harga = models.CharField(max_length=50, default=None)
    gambar = models.ImageField(upload_to='static/img/', default=None)

    def getAllMakanan():
        return Makanan.objects.all()
    
