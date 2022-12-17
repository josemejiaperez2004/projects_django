#Importaciones
from rest_framework import serializers
from .models import Producto
#Clase que serializa y descerializa cada registro
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        #campos que contien cada registro
        fields = (
            "id",
            "reference",
            "marca",
            "precio",
            "clasificacion",
            "imagen"
        )