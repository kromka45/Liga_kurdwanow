# Generated by Django 4.2.2 on 2023-06-19 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0003_zespol_punkty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zespol',
            name='punkty',
        ),
    ]
