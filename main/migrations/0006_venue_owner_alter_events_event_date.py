# Generated by Django 4.0.5 on 2022-07-14 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_events_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Venue Owner'),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.CharField(max_length=200, verbose_name='event_date'),
        ),
    ]
