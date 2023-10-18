from django.urls import path

from Joinus.views import Caricamento_candidatura, Conferma_candidatura, CandidaturaListView

urlpatterns = [
    path('candidatura/', Caricamento_candidatura.as_view(), name='caricamento_candidatura'),
    path('candidatura_inviata/', Conferma_candidatura, name='Candidaturainviata'),
    path('lista_candidature/', CandidaturaListView.as_view(), name='Candidature')
]