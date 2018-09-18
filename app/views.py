"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'background':'main_background',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'background':'main_background',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/aboutmain.html',
        {
            'title':'About',
            'background':'main_background',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
    )

def photosMain(request):
    d = datetime(2013,11,4)
    start = yearsago(d.year)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/photographymain.html',
        {
            'title':'Photography',
            'background':'photomain_background',
            'year':datetime.now().year,
            'start':start.year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
        )

def designMain(request):
    d = datetime(2008,9,18)
    start = yearsago(d.year)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/designmain.html',
        {
            'title':'Design',
            'background':'designmain_background',
            'year':datetime.now().year,
            'start':start.year,
            'textcolor':'text-black',
            'navbarcolor':'navbar-light',
        }
        )

def designHardware(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/design-hardware.html',
        {
            'title':'Hardware',
            'background':'main_background',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
        )

def designSoftware(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/design-software.html',
        {
            'title':'Software',
            'background':'main_background',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
        )

def photosPeople(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/photography-people.html',
        {
            'title':'People',
            'background':'main_background',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
        )

def photosPlaces(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/photography-places.html',
        {
            'title':'Places',
            'background':'main_background',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
        )

def photosWeddings(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/photography-weddings.html',
        {
            'title':'Weddings',
            'background':'main_background',
            'year':datetime.now().year,
            'textcolor':'text-white',
            'navbarcolor':'navbar-dark',
        }
        )

def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29 # can be removed
        return from_date.replace(month=2, day=28, year=from_date.year-years)