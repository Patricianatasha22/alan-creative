# Generated by Django 4.1.2 on 2023-01-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_pesanan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makanan',
            name='harga',
            field=models.IntegerField(default=None, max_length=50),
        ),
    ]
