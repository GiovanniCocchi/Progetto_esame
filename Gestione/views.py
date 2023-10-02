from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Photoapp.forms import CreaServizio


# Create your views here.


class Prenotazione_Servizio(CreateView):
    form_class = CreaServizio
    template_name ="Crea_servizio.html"
    success_url = reverse_lazy("ServizioPrenotato")

def ServizioPrenotato(request):
    return render(request, template_name="Servizio_prenotato.html")



