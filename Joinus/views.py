from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.datetime_safe import date
from django.views.generic import CreateView, ListView

from Joinus.models import Candidatura
from Photoapp.forms import CaricaCandidatura


# Create your views here.
class Caricamento_candidatura(CreateView):
    form_class = CaricaCandidatura
    template_name ="candidatura.html"
    success_url = reverse_lazy("Candidaturainviata")



    def form_valid(self, form):
        print("provo a validare il form")
        form.instance.data= date.today()
        # Se la data è disponibile, salva il servizio e reindirizza all'URL di successo
        return super().form_valid(form)


def Conferma_candidatura(request):
    return render(request, template_name='candidatura_inviata.html')

class CandidaturaListView(LoginRequiredMixin, ListView):
    model = Candidatura
    template_name = 'candidatura_list.html'
    context_object_name = 'candidature'
