from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    path('carica_immagine/<utente_pk>', carica_immagine.as_view(), name='carica_immagine'),
    path('Conferma_caricamento.html', Conferma_caricamento, name='ImmagineCaricata'),
    path('Immagini/', ImmaginiListView.as_view(), name='immagine-list'),
    path('Prenotazione/<utente_pk>/', Prenotazione_Servizio.as_view(), name='Prenotazione'),
    path('cancella_servizio/<int:pk>/', ServizioDeleteView.as_view(), name='CancellaServizio'),
    # effettuata una prenotazione, viene redirectato alla home del cliente
    path('Servizio_prenotato/', ServizioPrenotato, name='ServizioPrenotato'),
    #visualizza servizi prenotati da se Cliente
    path('Servizi_prenotati/', ServizioListView.as_view(), name='servizio-list'),
    path('Immagini_ph/', ImmaginiListViewph.as_view(), name='immagine-list_ph'),
    path('scarica/<immagine_pk>/', scarica, name='scarica_foto'),
    path('modifica/<immagine_pk>/', ImmagineEditView.as_view(), name='modifica_foto'),
    path('scarica_modificata/<immagine_pk>/', scarica_modificata, name='scarica_foto_modificata'),
] \
              #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
