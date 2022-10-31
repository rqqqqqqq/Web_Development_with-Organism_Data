# Generated by Django 3.2.5 on 2022-01-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organism_api', '0004_domain_protein_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protein',
            name='domains',
        ),
        migrations.AddField(
            model_name='protein',
            name='domains',
            field=models.ManyToManyField(through='organism_api.Domain_protein_link', to='organism_api.Domain'),
        ),
    ]
