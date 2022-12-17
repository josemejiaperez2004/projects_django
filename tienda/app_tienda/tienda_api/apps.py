#Importaciones
from django.apps import AppConfig

#Configuracion para que djanfo reconozca la API
class TiendaApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tienda_api'
