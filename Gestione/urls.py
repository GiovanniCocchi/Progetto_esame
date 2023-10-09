from django.contrib import admin
from django.urls import path, re_path

from .views import *

urlpatterns = [

    path('carica_immagine/<utente_pk>', carica_immagine.as_view(), name='carica_immagine'),
    path('Conferma_caricamento.html', Conferma_caricamento, name='ImmagineCaricata'),
    path('Immagini/', ImmaginiListView.as_view(), name='immagine-list'),
    #path('Download/',Download,name='scarica_immagini'),
    #path('Pagina_utente/', Pagina_utente, name='Pagina_utente'),
    #path('download/<str:file_name>/', download_file, name='download_file'),
    path('Prenotazione/<utente_pk>/', Prenotazione_Servizio.as_view(), name='Prenotazione'),
    path('cancella_servizio/<int:pk>/', ServizioDeleteView.as_view(), name='CancellaServizio'),
    # effettuata una prenotazione, viene redirectato alla home del cliente
    path('Servizio_prenotato/', ServizioPrenotato, name='ServizioPrenotato'),
    #visualizza servizi prenotati da se Cliente
    path('Servizi_prenotati/', ServizioListView.as_view(), name='servizio-list'),
    #path('servizio/<int:pk>/delete/', ServizioDeleteView.as_view(), name='servizio-delete'),
]
