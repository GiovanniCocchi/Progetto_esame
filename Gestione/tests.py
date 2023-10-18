
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Servizio

class PrenotazioneServizioTests(TestCase):
    def setUp(self):
        # Crea un utente per il test
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_utente_inserisce_data_precedente_ad_oggi(self, utente_pk=10):
        # Effettua il login con l'utente creato
        self.client.login(username='testuser', password='testpass')

        # Simula la creazione di un servizio con una data precedente ad oggi
        response = self.client.post(reverse("Prenotazione", kwargs={'utente_pk': utente_pk}), {
            'data': '2020-01-01',
            'reflex': True,
            'actioncam': False,
            'drone': False,
        })

        # Verifica che il form non sia valido
        self.assertEqual(response.status_code, 200)

        # Verifica che nessun servizio sia stato salvato nel database
        self.assertEqual(Servizio.objects.count(), 0)



class PrenotazioneServizioTests2(TestCase):
    def setUp(self):
        # Crea un utente per il test
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_utente_inserisce_data_precedente_ad_oggi(self, utente_pk=10):
        # Effettua il login con l'utente creato
        self.client.login(username='testuser', password='testpass')

        # Simula la creazione di un servizio con una data precedente ad oggi
        response = self.client.post(reverse("Prenotazione", kwargs={'utente_pk': utente_pk}), {
            'data': '2025-01-01',
            'reflex': False,
            'actioncam': False,
            'drone': False,
        })

        # Verifica che il form non sia valido
        self.assertEqual(response.status_code, 200)

        # Verifica che nessun servizio sia stato salvato nel database
        self.assertEqual(Servizio.objects.count(), 0)


class PaginaLoggatoTests(TestCase):
    def setUp(self):
        # Crea un utente per il test
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_caricamento_pagina(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('Loggato'), follow=True)

        # Verifica che la risposta abbia uno status code 200 (OK)
        self.assertEqual(response.status_code, 200)

        #print(response.content.decode('utf-8'))

        # Verifica che il contenuto della pagina contenga il testo "Benvenuto"
        self.assertContains(response, 'Benvenuto testuser')

        # Puoi anche verificare che un certo template sia stato utilizzato
        self.assertTemplateUsed(response, 'Utente_loggato.html')
