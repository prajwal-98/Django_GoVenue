from django.urls import path
from . import views

urlpatterns = [
    # path converters
    # int:numbers
    # str:string
    # path:whole urls/
    # slug:hyphen-and_underscore_stuff
    # UUID:universally unique identifier

    path('', views.home, name='home'),
    path("calender/", views.calender, name='calender'),
    path("events/", views.all_events, name="event-list"),
    path('add_event/', views.add_event, name="add-event"),
    path('update_event/<event_id>', views.update_event, name='update-events'),
    path('list_venue/', views.list_venue, name="list-venue"),
    path('venue/', views.venue, name="venue"),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('update_venue/<venue_id>', views.update_venues, name='update-venues'),
    path('search_venues/', views.search_venues, name='search-venues'),
    path('delete_event/<event_id>', views.delete_event, name='delete-events'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venues'),
    path('venue_text', views.venue_text, name='venue-text'),
    path('venue_csv', views.venue_csv, name='venue-csv'),
    path('venue_pdf', views.venue_pdf, name='venue-pdf'),
    path('my_event', views.my_event, name='my-event'),
    path('search_event', views.search_event, name='search-event'),
    path('admin_approval', views.admin_approval, name='admin_approval'),
    path('venue_events/<venue_id>', views.venue_events, name='venue-events'),
    path('show_event/<event_id>', views.show_event, name='show-event'),
]
