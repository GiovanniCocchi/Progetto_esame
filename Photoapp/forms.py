# FILE NEL QUALE METTO LE PAGINE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django import forms
from django.forms import DateInput

from Gestione.models import Servizio, Immagine


class CreaCliente(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit)
        g = Group.objects.get(name="cliente")
        g.user_set.add(user)
        return user

class CreaServizio(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "inserisci_servizio"
    helper.form_method = "POST"
    helper.add_input(Submit('submit', 'submit'))

    def __init__(self, *args, **kwargs):
        super(CreaServizio, self).__init__(*args, **kwargs)
        # Filtra gli utenti del gruppo "fotografi" per il campo "fotografi"
        self.fields['fotografi'].queryset = User.objects.filter(groups__name='fotografo')

    class Meta:
        model = Servizio
        fields=['data','reflex', 'actioncam', 'drone', 'fotografi']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
        }

class Caricaimmagine(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "carica_immagine"
    helper.form_method = "POST"
    helper.add_input(Submit('submit', 'submit'))

    def __init__(self, *args, **kwargs):
        super(Caricaimmagine, self).__init__(*args, **kwargs)
        # Filtra gli utenti del gruppo "fotografi" per il campo "fotografi"
        self.fields['fotografi'].queryset = User.objects.filter(groups__name='fotografo')

    class Meta:
        model = Immagine
        fields=['Descrizione','immagine', 'fotografi']


class ImmagineUpdateView(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = "modifica_immagine"
    helper.form_method = "POST"
    helper.add_input(Submit('submit', 'submit'))

    class Meta:
        model= Immagine
        fields= ['foto_modificata']

    def save(self, commit=True):
        istanza = super().save(commit=False)
        istanza.stato = 'modificata'  # Imposta lo stato a 'modificata'
        if commit:
            istanza.save()
        return istanza

