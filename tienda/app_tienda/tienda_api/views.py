#Importaciones
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.
class ProductoListApiView(APIView):
    # 1. Lista de all products
    def get(self, request, *args, **kwargs):

        #List all products for given requested user
        productos = Producto.objects
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK
    )

    # 2. Un nuevo registro
    def post(self, request, *args, **kwargs):
        #Listado de campos que se motrara
        data = {
            'reference': request.data.get('reference'),
            'marca': request.data.get('marca'),
            'precio': request.data.get('precio'),
            'clasificacion': request.data.get('clasificacion'),
            'imagen': request.data.get('imagen')
        }
        #Serializacion de cada registro y descerializacion
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#Detalles de producto
class ProductoDetailApiView(APIView):

    # 1. Metodo auxiliar para obtener el id de producto
    def get_object(self, producto_id):
        try:
            return Producto.objects.get(id = producto_id)
        
        except Producto.DoesNotExist:
            return none

    # 2. Recuperar el producto de acuerdo al id
    def get(self, request, producto_id, *args, **kwargs):
        producto_instance = self.get_object(producto_id)
        if not producto_instance:
            return Response(
                {"res": "El objeto no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Serializacion de registro
        serializer = ProductoSerializer(producto_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # 3. Actualiza el elemento Producto con el producto_id si existe
    def put(self, request, producto_id, *args, **kwargs):
        producto_instance = self.get_object(producto_id)
        if not producto_instance:
            return Response(
                {"res": "objeto no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        #Listado de campos que se actualizara
        data = {
            'reference': request.data.get('reference'),
            'marca': request.data.get('marca'),
            'precio': request.data.get('precio'),
            'clasificacion': request.data.get('clasificacion'),
            'imagen': request.data.get('imagen')
        }

        #serializacion del registro
        serializer = ProductoSerializer(
            instance = producto_instance,
            data=data,
            partial=True
        )
        #si se serializa bien se guardara el cambio, de lo contrario error 404
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    # 4. Elimina producto con id
    def delete(self, request, producto_id, *args, **kwargs):
        producto_instance = self.get_object(producto_id)
        if not producto_instance:
             Response(
                {"res": "Objeto no existe"},
                status=status.HTTP_400_BAD_REQUEST
             )
        producto_instance.delete()
        return Response(
            {"res": "objeto eliminado"},
            status=status.HTTP_200_OK
        )

#Vista de todos los registro con el mismo valor de clasificacion
class ProductoDetailClasificacion(APIView):
    #Metodo que muestra los registro con el mismo valor de clasificacion
    def get(self, request, producto_clasif, *args, **kwargs):
        productos = Producto.objects.filter(clasificacion=producto_clasif)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    