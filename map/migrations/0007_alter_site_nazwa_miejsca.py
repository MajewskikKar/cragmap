# Generated by Django 4.2.7 on 2023-12-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_site_nazwa_miejsca_alter_site_nazwa_strony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nazwa_miejsca',
            field=models.CharField(help_text="Nazwa miejsca, tożsama z 'crags'", max_length=100),
        ),
    ]
