import os
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib import messages
from django.http import FileResponse, HttpResponseNotFound, response
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from Gestione.models import Servizio, Immagine
from Photoapp import settings
from Photoapp.forms import CreaServizio, Caricaimmagine, ImmagineUpdateView
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
        reflex = form.cleaned_data['reflex']
        actioncam= form.cleaned_data['actioncam']
        drone= form.cleaned_data['drone']
        if not reflex and not actioncam and not drone:
            form.add_error('reflex', 'Scegli almeno uno strumento')
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

class carica_immagine(CreateView,LoginRequiredMixin):
    form_class = Caricaimmagine
    template_name = "Carica_immagine.html"
    success_url = reverse_lazy("ImmagineCaricata")

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
        cliente = self.get_user()
        form.instance.cliente = cliente

        # salva la foto e reindirizza all'URL di successo
        return super().form_valid(form)

def Conferma_caricamento(request):
    return render(request, template_name="Immagine_caricata.html")

class ImmaginiListView(LoginRequiredMixin, ListView):
    model = Immagine
    template_name = 'Immagine_list.html'
    context_object_name = 'Immagini'

    def get_queryset(self):
        # Ottieni l'oggetto utente loggato
        user = self.request.user

        # Filtra i servizi associati all'utente loggato
        queryset = Immagine.objects.filter(cliente_id=user)

        return queryset


class ImmaginiListViewph(LoginRequiredMixin,ListView):
    model = Immagine
    template_name = 'immagine_list.html'
    context_object_name = 'Immagini'

    def get_queryset(self):
        # Ottieni l'oggetto utente loggato
        user = self.request.user
        print("sono qui")
        print(user)
        userid=user.id
        # Filtra i servizi associati all'utente loggato
        queryset = Immagine.objects.filter(fotografi=userid,stato='da modificare')
        print(userid)

        return queryset

def scarica(request, immagine_pk):
    """immagine=Immagine.objects.get(pk=immagine_pk)
    with open(str(immagine.immagine), "rb") as ciucciacazzi:
        response=FileResponse(ciucciacazzi)
    return response"""
    immagine = get_object_or_404(Immagine, pk=immagine_pk)
    response = FileResponse(open(str(immagine.immagine), 'rb'))
    return response

class ImmagineEditView(UpdateView):
    model = Immagine
    form_class = ImmagineUpdateView
    template_name = 'modifica_foto.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('immagine_pk')
        immagine = Immagine.objects.get(pk=pk)
        return immagine

    def form_valid(self, form):
        immagine = form.save(commit=False)
        # Ottieni l'immagine caricata dall'utente
        foto_modificata = self.request.FILES.get('foto_modificata')
        if foto_modificata:
            immagine.foto_modificata = foto_modificata
            print("CI SONO")

        immagine.stato = 'modificata'
        immagine.save()

        messages.success(self.request, 'Modifiche salvate con successo!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("immagine-list_ph")


def scarica_modificata(request, immagine_pk):
    """immagine=Immagine.objects.get(pk=immagine_pk)
    with open(str(immagine.immagine), "rb") as ciucciacazzi:
        response=FileResponse(ciucciacazzi)
    return response"""
    immagine = get_object_or_404(Immagine, pk=immagine_pk)
    response = FileResponse(open(str(immagine.foto_modificata), 'rb'))
    return response


class ImmagineDeleteView(DeleteView):
    model = Immagine
    template_name = "cancella_immagine.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        immagine = "Immagine"
        ctx["immagine"] = immagine
        return ctx

    def get_success_url(self):
        return reverse("immagine-list")