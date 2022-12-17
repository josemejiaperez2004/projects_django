#IMPORTACIONES
from django.urls import path
from .views import HomePageView

#Administrador de urls con sobrenombres
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #path('forgot_password', ForgotPasswordView.as_view(), name='forgot_password'),

]