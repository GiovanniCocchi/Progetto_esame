# COMANDI INIZIALI PER LA CREAZIONE DI GRUPPI
from django.contrib.auth.models import Group, Permission


def crea_gruppi():
    cliente, creato_ciente = Group.objects.get_or_create(name="cliente")
    fotografo, creato_fotografo = Group.objects.get_or_create(name="fotografo")

    lista_permessi_fotografo = ['change_servizio', 'delete_servizio']
    lista_permessi_cliente = ['add_servizio', 'delete_servizio']

    for perm in lista_permessi_fotografo:
        permesso = Permission.objects.get(codename=perm)
        fotografo.permissions.add(permesso)

    for perm in lista_permessi_cliente:
        permesso = Permission.objects.get(codename=perm)
        cliente.permissions.add(permesso)
