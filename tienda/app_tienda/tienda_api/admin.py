#Importaciones
from django.contrib import admin
from .models import Producto


# Register your models here.
#MotoAdmin
#Clase que administra cada registro creado
class ProductoAdmin(admin.ModelAdmin):
    #campos que contiene cada registro
    list_display = [
        "reference",
        "marca",
        "precio",
        "clasificacion",
        "imagen"
    ]
#administrador de las clases 
admin.site.register(Producto, ProductoAdmin)