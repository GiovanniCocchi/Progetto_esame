from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView

from Gestione.models import Servizio
from Photoapp.forms import CreaServizio
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class Prenotazione_Servizio(LoginRequiredMixin,CreateView):
    form_class = CreaServizio
    template_name ="Crea_servizio.html"
    success_url = reverse_lazy("ServizioPrenotato")

    def get_user(self):
        pk = self.kwargs.get('utente_pk')
        print(pk)
        try:
            user = User.objects.get(pk=pk)
            return user
        except Exception:
            print("blyad")
        return None


    def form_valid(self, form):
        print("provo a validare il form")
        # Verifica se esiste già un servizio prenotato nella data selezionata
        data_scelta = form.cleaned_data['data']

        servizi_nella_data = Servizio.objects.filter(data=data_scelta)


        if servizi_nella_data.exists():
           # Se ci sono già servizi prenotati nella data, comunica al cliente
           form.add_error('data', 'Il servizio è già prenotato per questa data.')
           return self.form_invalid(form)
        oggi = datetime.now()
        oggi2= datetime.date(oggi)
        if oggi2 > data_scelta:
            form.add_error('data', 'Scegli una data futura')
            return self.form_invalid(form)




        # Recuperiamo il cliente e lo impostiamo
        cliente = self.get_user()
        form.instance.cliente = cliente

        # Se la data è disponibile, salva il servizio e reindirizza all'URL di successo
        return super().form_valid(form)

class ServizioDeleteView(DeleteView):
    model = Servizio
    template_name = "cancella.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        servizio = "Servizio"
        ctx["servizio"] = servizio
        return ctx

    def get_success_url(self):
        return reverse("servizio-list")


def ServizioPrenotato(request):
    return render(request, template_name="Servizio_prenotato.html")

from django.contrib.auth.mixins import LoginRequiredMixin

class ServizioListView(LoginRequiredMixin, ListView):
    model = Servizio
    template_name = 'servizio_list.html'
    context_object_name = 'servizi'

    def get_queryset(self):
        # Ottieni l'oggetto utente loggato
        user = self.request.user

        # Filtra i servizi associati all'utente loggato
        queryset = Servizio.objects.filter(cliente=user)

        return queryset
"""
class ServizioDeleteView(LoginRequiredMixin, DeleteView):
    model = Servizio
    template_name = 'Cancella_servizio.html'
    success_url = reverse_lazy('servizio-list')  # Redirect dopo la cancellazione

    def get_queryset(self):
        # Filtra i servizi associati all'utente loggato
        return Servizio.objects.filter(cliente=self.request.user)
    """




