from django.db import models



# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    stock = models.IntegerField(max_length=5)
    fecha_vencimiento = models.DateField()
    fecha_entrada = models.DateField()






