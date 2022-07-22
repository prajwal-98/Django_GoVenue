from django import forms
from django.forms import ModelForm
from .models import Venue, events


# create a venue form

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone', 'web', 'email_Address', 'venue_image')
        labels = {
            'name': 'Enter Your venue here',
            'address': '',
            'phone': '',
            'email_Address': '',
            'web': '',
            'venue_image': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Web'}),
            'email_Address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


# admin superuser EventForm
class EventFormAdmin(ModelForm):
    class Meta:
        model = events
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            'name': '',
            'event_date': '',
            'venue': 'venue',
            'manager': '',
            'attendees': 'Attendees',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'event_date'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'venue'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control ', 'placeholder': 'attendees'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }


# User Event Form
class EventForm(ModelForm):
    class Meta:
        model = events
        fields = ('name', 'event_date', 'venue', 'attendees', 'description')
        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'attendees': 'Attendees',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
