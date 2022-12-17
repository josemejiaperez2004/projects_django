#importaciones
from django.contrib import admin
from .models import Moto


# Register your models here.
#Clase para administrar los registros
class MotoAdmin(admin.ModelAdmin):

    #campos de cada registro
    list_display = (
        "reference",
        "tradermark",
        "model",
        "price",
        "image",
        "supplier",
    )
    #administrador de url
admin.site.register(Moto, MotoAdmin)