#importaciones
from rest_framework import serializers
from .models import Moto

#Clase para seliarizar cada regitro
class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        #campos de cada registro
        fields = (
            "id",
            "reference",
            "tradermark",
            "model",
            "price",
            "image",
            "supplier",
        )