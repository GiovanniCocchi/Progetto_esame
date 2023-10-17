"""
URL configuration for Photoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from .initcmd import crea_gruppi
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^$|^/$|home/$", page_with_static, name='Home'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("Utente_loggato/", Utenteloggato ,name="Loggato"),
    path('Registrazione_Cliente/pagina-di-conferma.html', Conferma_caricamento_cliente ,name='Conferma_caricamento_cliente'),
    path('Registrazione_Cliente/', CreaUtente.as_view(), name='Crea_cliente'),
    path('Gestione/', include("Gestione.urls")),
    path('Calendario/', Calendario_page.as_view(), name="Calendario"),
    path('chat/', include("chat.urls"))
]
crea_gruppi()

