# Generated by Django 4.2 on 2023-10-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestione', '0003_immagine_cliente_immagine_fotografi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immagine',
            name='foto_modificata',
            field=models.ImageField(blank=True, null=True, upload_to='immagini_da_modificare/'),
        ),
    ]