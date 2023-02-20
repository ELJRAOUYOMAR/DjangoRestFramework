# Generated by Django 4.1.2 on 2022-12-11 13:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_guest_movie_reservation_delete_jsonformat'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 11, 14, 5, 27, 579891)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='hall',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='tickets.guest'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='tickets.movie'),
        ),
    ]
