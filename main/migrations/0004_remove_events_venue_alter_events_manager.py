# Generated by Django 4.0.5 on 2022-07-07 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_venue_email_address_alter_venue_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='venue',
        ),
        migrations.AlterField(
            model_name='events',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
