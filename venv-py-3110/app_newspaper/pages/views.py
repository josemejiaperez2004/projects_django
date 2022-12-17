#IMPORTACIONES
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# Vista de la pantalla Home 
class HomePageView(TemplateView):
    template_name = 'home.html'


#vista de olvido de contraseña
#class ForgotPasswordView(TemplateView):
#    template_name = 'registration/password_reset_form.html'

