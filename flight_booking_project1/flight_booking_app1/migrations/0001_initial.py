# Generated by Django 4.2 on 2023-11-19 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=10, unique=True)),
                ('flight_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('seat_count', models.IntegerField(default=60)),
                ('booked_seats', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking_app1.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
