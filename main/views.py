from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import events, Venue

# Import User Model From Django
from django.contrib.auth.models import User
from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponse
import csv
from django.contrib import messages

# import PDF stuff
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io

# import pagination stuff
from django.core.paginator import Paginator


def home(request):
    return render(request, 'main/home.html')


# generate a PDF file for Venue list
def venue_pdf(response):
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    venues = Venue.objects.all()
    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.phone)
        lines.append(venue.email_Address)
        lines.append(' ')
    # loop
    for line in lines:
        textob.textLine(line)
    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # return something
    return FileResponse(buf, as_attachment=True, filename='venue.pdf')


# generate a CSV file for Venue list
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response[''] = 'attachment; filename = venues.csv'
    # create a csv write
    writer = csv.writer(response)
    # designate the model
    venues = Venue.objects.all()
    # add column heading to csv file
    writer.writerow(['Venue Name', 'Address', 'Phone', 'Email'])
    # loop through and output
    for venues in venues:
        writer.writerow([venues.name, venues.address, venues.phone, venues.email_Address])
    # response.writelines(lines)
    return response


# generate a text file for Venue list
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = venues.txt'
    # designate the model
    venues = Venue.objects.all()
    # create a blank list
    lines = []
    # loop through and output
    for venue in venues:
        lines.append(f'{venue}\n {venue.name}\n {venue.address}\n {venue.phone}\n {venue.email_Address}\n\n\n')
    response.writelines(lines)
    return response


def all_events(request):
    event_list = events.objects.all()
    return render(request, 'main/event_list.html', {'event_list': event_list})


def calender(request, year=datetime.now().year, month=datetime.now().month):
    name = "Prajwal"
    # Get current time
    time = datetime.now().strftime('%I:%M %p')
    # create a calendar

    cal = HTMLCalendar().formatmonth(year, month)
    # Query the Events Model For Dates
    event_list = events.objects.filter(event_date__year =year, event_date__month=month)
    return render(request, 'main/calender.html', {"name": name, "year": year, "month": month, "cal": cal, "time": time, "event_list": event_list})


def search_event(request):
    if request.method == "POST":
        searched = request.POST['searched']
        event = events.objects.filter(name__contains=searched)

        return render(request, 'main/search_events.html', {'searched': searched, 'event': event})
    else:
        return render(request, 'main/search_events.html', {})


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'main/search_venues.html',
                      {'searched': searched, 'venues': venues})
    else:
        return render(request, 'main/search_venues.html', {})


def add_event(request):
    submitted = False

    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                # form.save()
                event = form.save(commit=False)
                event.manager = request.user  # logged in user
                event.save()
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        # Just Going To The Page, Not Submitting
        if request.user.is_superuser:
            form = EventFormAdmin()
        else:
            form = EventForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'main/add_event.html', {'form': form, 'submitted': submitted})


def update_event(request, event_id):
    event = events.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect("event-list")

    return render(request, 'main/update_event.html',
                  {'event': event, 'form': form})


def delete_event(request, event_id):
    event = events.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, "Event Deleted!!")
        return redirect('event-list')
    else:
        messages.success(request, "You Aren't Authorized To Delete This Event!")
        return redirect('event-list')


def venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            # logged in user
            venue.owner = request.user.id
            venue.save()
            # form.save()
            return HttpResponseRedirect('/venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/venue.html', {'form': form, 'submitted': submitted})


def update_venues(request, venue_id):
    venues = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, request.FILES or None, instance=venues)
    if form.is_valid():
        form.save()
        return redirect("list-venue")
    return render(request, 'main/update_venue.html',
                  {'venues': venues, 'form': form})


def delete_venue(request, venue_id):
    context = {}
    venue_del = Venue.objects.get(pk=venue_id)
    if request.method == "POST":
        venue_del.delete()
        return redirect('list-venue')
    return render(request, "main/delete_venue.html", context)


def list_venue(request):
    # venue_list = Venue.objects.all().order_by('?') # random order
    venue_list = Venue.objects.all().order_by('name')
    # setup pagination
    p = Paginator(Venue.objects.all(), 5)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = 'a' * venues.paginator.num_pages

    return render(request, 'main/list_venue.html',
                  {'venue_list': venue_list,
                   'venues': venues,
                   'nums': nums})


def my_event(request):
    if request.user.is_authenticated:
        me = request.user.id
        event = events.objects.filter(attendees=me)
        return render(request, 'main/my_events.html', {"event": event})
    else:
        messages.success(request, "You Aren't Authorized To View This Page")
        return redirect('home')


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=venue.owner)

    # Grab the events from that venue
    event = venue.events_set.all()

    return render(request, 'main/show_venue.html', {'venue': venue, 'venue_owner': venue_owner, 'event': event})


def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'main/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'main/search_venues.html', {})


def admin_approval(request):
    # Get The Venues
    venue_list = Venue.objects.all()
    # Get Counts
    event_count = events.objects.all().count()
    venue_count = Venue.objects.all().count()
    user_count = User.objects.all().count()

    event_list = events.objects.all().order_by('-event_date')
    if request.user.is_superuser:
        if request.method == "POST":
            # Get list of checked box id's
            id_list = request.POST.getlist('boxes')

            # Uncheck all events
            event_list.update(approved=False)

            # Update the database
            for x in id_list:
                events.objects.filter(pk=int(x)).update(approved=True)

            # Show Success Message and Redirect
            messages.success(request, "Event List Approval Has Been Updated!")
            return redirect('event-list')



        else:
            return render(request, 'main/admin_approval.html',
                          {"event_list": event_list,
                           "event_count": event_count,
                           "venue_count": venue_count,
                           "user_count": user_count,
                           "venue_list": venue_list})
    else:
        messages.success(request, "You aren't authorized to view this page!")
        return redirect('home')

    return render(request, 'main/admin_approval.html')


# Show Event
def show_event(request, event_id):
    event = events.objects.get(pk=event_id)
    return render(request, 'main/show_event.html', {
        "event": event
    })


# Show Events In A Venue
def venue_events(request, venue_id):
    # Grab the venue
    venue = Venue.objects.get(id=venue_id)
    # Grab the events from that venue
    events = venue.event_set.all()
    if events:
        return render(request, 'main/venue_events.html', {
            "events": events
        })
    else:
        messages.success(request, "That Venue Has No Events At This Time...")
        return redirect('admin_approval')
