# Generated by Django 4.2.6 on 2023-10-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cognome', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('reflex', models.BooleanField()),
                ('actioncam', models.BooleanField()),
                ('drone', models.BooleanField()),
                ('patente', models.BooleanField()),
                ('album', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Candidature',
            },
        ),
    ]
