# Generated by Django 4.2.2 on 2023-06-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0007_remove_zespol_punkty'),
    ]

    operations = [
        migrations.AddField(
            model_name='zespol',
            name='punkty',
            field=models.IntegerField(default=0),
        ),
    ]
