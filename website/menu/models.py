from django.db import models
# Create your models here.

class Makanan(models.Model):

    class meta:
        db_table = 'makanan'

    nama = models.CharField(max_length=50, default=None)
    harga = models.IntegerField(max_length=50, default=None)
    gambar = models.ImageField(upload_to='static/img/', default=None)

    def getAllMakanan():
        return Makanan.objects.all()
    
    def getMakananByID(id):
        makanan = Makanan.objects.get(id = id)

        return makanan
    
    def deleteMakanan(id):
        makanan = Makanan.getMakananByID(id)
        makanan.delete()

        return True
    
class Pesanan(models.Model):
    class meta:
        db_table = 'pesanan'
    
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default = 1)

    @classmethod
    def createPesanan(cls, id):
        makanan = Makanan.getMakananByID(id)

        pesanan = cls(makanan=makanan)

        pesanan.save()

        return True
    
    @property
    def totalHarga(self):
        return self.makanan.harga * self.jumlah
        
    def getAllMakananUnik():
        return list(Pesanan.objects.all().values_list('makanan', flat=True)) 
    
    def getAllPesanan():
        return Pesanan.objects.all()
    
    def getPesananByID(id):
        pesanan = Pesanan.objects.get(makanan=id)
        return pesanan
    
    def updateJumlah(id):

        pesanan = Pesanan.getPesananByID(id)
        pesanan.jumlah += 1

        pesanan.save()

        return True
    
    def clearSale():
        pesanan = Pesanan.objects.all().delete()
        return True
    
    def getTotal():
        pesanans = Pesanan.getAllPesanan()
        total = 0
        for pesanan in pesanans:
            total += pesanan.totalHarga
        
        return total

    



    