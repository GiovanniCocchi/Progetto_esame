# VISTE CHE CHIAMO QUANDO RAGGIUNGO GLI URL
from django.shortcuts import render


def page_with_static(request):
    return render(request, template_name="home.html")