# Generated by Django 5.0.14 on 2025-07-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEG', '0002_alter_a_beskrivelse'),
    ]

    operations = [
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('ord', models.CharField(max_length=50)),
                ('beskrivelse', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('ord', models.CharField(max_length=50)),
                ('beskrivelse', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('ord', models.CharField(max_length=50)),
                ('beskrivelse', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='E',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('ord', models.CharField(max_length=50)),
                ('beskrivelse', models.TextField(blank=True)),
            ],
        ),
    ]
