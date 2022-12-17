#importaciones
from django.urls import path
from .views import MotoListApiView, MotoDetailApiView
#rutas para la respectiva navegacion y vitas de la API
urlpatterns = [
    path('', MotoListApiView.as_view(), name="Moto_list"),
    path('<int:moto_id>/', MotoDetailApiView.as_view(), name="Moto_detail")
]