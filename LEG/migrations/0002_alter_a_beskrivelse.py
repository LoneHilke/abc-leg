# Generated by Django 5.0.14 on 2025-07-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='beskrivelse',
            field=models.TextField(blank=True),
        ),
    ]
