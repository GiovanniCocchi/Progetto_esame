# FILE NEL QUALE METTO LE PAGINE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class CreaCliente(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit)
        g = Group.objects.get(name="cliente")
        g.user_set.add(user)
        return user
