# Generated by Django 3.2.5 on 2022-01-09 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organism_api', '0002_auto_20220107_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protein',
            name='domains',
        ),
        migrations.AddField(
            model_name='protein',
            name='domains',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='organism_api.domain'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Domain_protein_link',
        ),
    ]
