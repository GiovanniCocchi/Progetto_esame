# Progetto_esame
Per far partire il progetto sono necessari:
python 9.0
django
pycharm 

Una volta installati:
- clonare la directory
- creare un ambiente virtuale pipenv shell
- installare Django con pipenv install Django
- installare bootstrap, crispy forms e daphne
- pipenv install django-bootstrap4
- pipenv install django-crispy-forms
- piennv install daphne

eseguire le migrazioni
- python manage.py migrate

creare il superutente:
- python manage.py createsuperuser

runnare il server con il comando
- python manage.py runserver
  
creare due utenti e con il pannello admin assegnare ad uno il gruppo "fotografi"
