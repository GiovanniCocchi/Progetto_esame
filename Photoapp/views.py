# VISTE CHE CHIAMO QUANDO RAGGIUNGO GLI URL
import json
import os
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreaCliente
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.staticfiles import finders
from django.core import serializers
from django.db.models import Q
from django.http import Http404, FileResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Gestione.models import *
#from .form import ImmagineForm, RegistrazioneClienteForm, PrenotazioneServizioForm, CancellaServizioForm
from django.shortcuts import redirect

def page_with_static(request):
    return render(request, template_name="home.html")

class Calendario_page(ListView):
    model = Servizio
    template_name = "Calendario.html"
    context_object_name = "servizi"

    def get_queryset(self):
        parameters = self.request.GET
        print("parameters: " + str(parameters))
        if 'year' in parameters and 'month' in parameters:
            year = int(parameters['year'])
            month = int(parameters['month'])
            print("year: " + str(year))
            print("mounth: " + str(month))
            if (month < 1 or month > 12 or year < 1980):
                data_odierna = datetime.now().date()
                year = str(data_odierna.year)
                month = str(data_odierna.month)
            servizi = Servizio.objects.filter(Q(data__year=year) & Q(data__month=month))
        else:
            data_odierna = datetime.now().date()
            servizi = Servizio.objects.filter(Q(data__year=data_odierna.year) & Q(data__month=data_odierna.month))
        data = serializers.serialize('json', servizi)
        data = json.loads(
            data)  # [{'data': '2023-09-06', 'reflex': True, 'actioncam': True, 'drone': False, 'fotografi': [1]}]
        # let servizi = [{'data': '2023-09-06', 'reflex': True, 'actioncam': True, 'drone': False, 'fotografi': [1]}];
        data = [
            {
                'data': servizio["fields"]["data"],  # string indices must be integers, not 'str'
                'reflex': servizio["fields"]["reflex"],
                'actioncam': servizio["fields"]["actioncam"],
                'drone': servizio["fields"]["drone"],
                'fotografi': servizio["fields"]["fotografi"],
            } for servizio in data
        ]
        print(data)
        data = json.dumps(data)

        # [{"model": "Photoapp.servizio", "pk": 1, "fields": {"data": "2023-09-06", "reflex": true, "actioncam": true, "drone": false, "cliente": 1, "fotografi": [1]}}]
        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        parameters = self.request.GET
        """
         let servizi = [{'drone': False, 'reflex': True, 'actioncam': True, 'data': datetime.date(2023, 9, 6)}];
        """
        if 'year' in parameters and 'month' in parameters:
            year = parameters['year']
            month = parameters['month']
            if (int(month) < 1 or int(month) > 12 or int(year) < 1980):
                data_odierna = datetime.now().date()
                year = str(data_odierna.year)
                month = str(data_odierna.month)
        else:
            data_odierna = datetime.now().date()
            year = str(data_odierna.year)
            month = str(data_odierna.month)
        context["date"] = year + "-" + month + "-01"
        return context


"""@require_GET
def get_day_info(request):
    year, month = int(request.GET['year']), int(request.GET['month'])
    servizi = Servizio.objects.filter(Q(data__year=year) & Q(data__month=month))
    servizi_json = []
    for s in servizi:
        servizio_json = {
            'Relflex': s.reflex,
            'Drone': s.drone,
            'ActionCam': s.actioncam,
            'Fotografi': [
                f.nome for f in s.fotografi
            ]
        }
        servizi_json.append(servizio_json)

    data = {
        'servizi': servizi_json
    }
    # Return the dictionary as a JSON response
    return JsonResponse(data)  # TODO Implementarlo nel html"""


class CreaUtente(CreateView):
    form_class = CreaCliente
    template_name = "registrazione.html"
    success_url = reverse_lazy("Conferma_caricamento_cliente")

def Conferma_caricamento_cliente(request):
    return render(request, template_name="pagina-di-conferma.html")

@login_required
def Utenteloggato(request):
    pk = request.user.pk
    context = {
        'user_pk': pk,
    }
    return render(request, template_name="Utente_loggato.html",context=context)



