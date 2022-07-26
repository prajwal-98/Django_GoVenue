# Generated by Django 4.0.5 on 2022-07-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_myclubuser_venue_events_attendees_alter_events_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email_Address',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='zip_code',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
