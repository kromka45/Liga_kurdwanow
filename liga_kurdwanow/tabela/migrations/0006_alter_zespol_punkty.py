# Generated by Django 4.2.2 on 2023-06-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0005_zespol_punkty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zespol',
            name='punkty',
            field=models.IntegerField(),
        ),
    ]
