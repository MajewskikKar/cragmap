# Generated by Django 4.2.7 on 2024-02-16 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_crag_nazwa_alter_site_crags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='crags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.crag'),
        ),
    ]