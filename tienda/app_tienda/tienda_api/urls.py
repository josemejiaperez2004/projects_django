#Importaciones
from django.urls import path
from .views import ProductoListApiView, ProductoDetailApiView, ProductoDetailClasificacion
#Rutas de cada vista que se verá en la API
#Se le pasa como parametro lo que se filtrará
urlpatterns = [
    path('', ProductoListApiView.as_view(), name="Producto_list"),
    path('<int:producto_id>/', ProductoDetailApiView.as_view(), name="Producto_detail"),
    path('<str:producto_clasif>/', ProductoDetailClasificacion.as_view(), name="producto_clasif")
]