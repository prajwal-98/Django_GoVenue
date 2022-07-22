from django.contrib import admin
from .models import Venue, MyClubUser, events
from django.contrib.auth.models import Group

# Register your models here.

# admin.site.register(Venue)
admin.site.register(MyClubUser)
# remove Groups from admin page
admin.site.unregister(Group)
# admin.site.register(events)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'web', 'email_Address')
    ordering = ('-name',)
    search_fields = ('name', 'address')


@admin.register(events)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager', 'approved')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('event_date',)
