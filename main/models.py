from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):
    name = models.CharField('Venue_name', max_length=200)
    address = models.CharField('address', max_length=200)
    zip_code = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    web = models.URLField(max_length=200, blank=True)
    email_Address = models.EmailField(max_length=200, blank=True)
    owner = models.IntegerField("Venue Owner", blank=False, default=1)
    venue_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField('user_email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class events(models.Model):
    name = models.CharField('event_name', max_length=200)
    event_date = models.DateTimeField('event_date', max_length=200)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    approved = models.BooleanField('approved', default=False)

    def __str__(self):
        return f'{self.name} {self.event_date}'

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped

    @property
    def Is_Past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing
