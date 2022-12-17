#importaciones
from django.db import models

# Create your models here.
#creacion de clase que contendra los campos de cada registro
class Moto(models.Model):
    id = models.AutoField(primary_key = True)
    reference = models.CharField(max_length = 30, blank = False, null = False)
    tradermark = models.CharField(max_length = 30, blank = False, null = False)
    model = models.CharField(max_length = 10, blank = False, null = False)
    price = models.IntegerField()
    image = models.CharField(max_length = 300, blank = False, null = False)
    supplier = models.CharField(max_length = 60, blank = False, null = False)

    def __str__(self):
        return self.reference