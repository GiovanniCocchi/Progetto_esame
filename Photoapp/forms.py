# FILE NEL QUALE METTO LE PAGINE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django import forms

from Gestione.models import Servizio


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

    class Meta:
        model = Servizio
        fields=['data','reflex', 'actioncam', 'drone', 'fotografi','cliente']

