# Generated by Django 4.2.7 on 2023-12-05 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_crag_site_delete_crags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='crags',
        ),
        migrations.AddField(
            model_name='site',
            name='crags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.crag'),
        ),
    ]