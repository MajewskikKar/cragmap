# Generated by Django 4.2.7 on 2023-12-05 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_alter_site_nazwa_miejsca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='nazwa_miejsca',
        ),
    ]
