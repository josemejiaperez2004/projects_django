#importaciones
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Moto
from .serializers import MotoSerializer

# Create your views here.

#Primer endPoint GET
class MotoListApiView(APIView):

    #1. Lista de registros
    def get(self, request, *args, **kwargs):
        
        #lista de todas las motos para entregar al usuario
        motos = Moto.objects
        serializer = MotoSerializer(motos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    #2. Nuevo Registro
    def post(self, request, *args, **kwargs):
        
        #envio de datos a la base de datos
        data = {

            'reference': request.data.get('reference'),
            'tradermark': request.data.get('tradermark'),
            'model': request.data.get('model'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }

        serializer = MotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MotoDetailApiView(APIView):

    #1. Metodo auxiliar para obtener el objeto con moto_id dado
    def get_object(self, moto_id):
        try:
            return Moto.objects.get(id=moto_id)
        except Moto.DoesNotExist:
            return None

    #2. Recupera el elemento Moto con moto_id dado
    def get(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MotoSerializer(moto_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #3. Actualiza el elemento Moto con moto_id dado, solo si existe
    def put(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


        #Registros
        data = {

            'reference': request.data.get('reference'),
            'tradermark': request.data.get('tradermark'),
            'model': request.data.get('model'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        #Serializacion
        serializer = MotoSerializer(
            instance = moto_instance,
            data= data,
            partial = True
        )

        #Si la serializacion es exitosa se guarda el cambio del registro
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #4. Elimina el elemento Moto con moto_id, si existe
    def delete(self, request, moto_id, *args, **kwargs):
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # funcion para eliminar el objeto
        moto_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
            

            

        
