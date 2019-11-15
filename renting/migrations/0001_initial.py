# Generated by Django 2.2.6 on 2019-11-15 08:24

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import renting.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Ciuadad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anfitrion',
                'verbose_name_plural': 'Anfitriones',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('max_guests', models.IntegerField()),
                ('img', models.ImageField(upload_to=renting.models.make_file_path)),
                ('img2', models.ImageField(upload_to=renting.models.make_file_path)),
                ('img3', models.ImageField(upload_to=renting.models.make_file_path)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='renting.City')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='renting.Host')),
            ],
            options={
                'verbose_name': 'Propiedad',
                'verbose_name_plural': 'Propiedades',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('guestName', models.CharField(max_length=120)),
                ('guestEmail', models.EmailField(max_length=80)),
                ('guests', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'Reserva de cliente',
                'verbose_name_plural': 'Reservas de cliente',
            },
        ),
        migrations.CreateModel(
            name='RentDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='renting.Property')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='renting.Reservation')),
            ],
            options={
                'verbose_name': 'Reserva por propiedad',
                'verbose_name_plural': 'Reservas por propiedad',
            },
        ),
    ]
