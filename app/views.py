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
        }
    )

def photosMain(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/photographymain.html',
        {
            'title':'Photography',
            'background':'main_background',
            'year':datetime.now().year,
        }
        )

def designMain(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/designmain.html',
        {
            'title':'Design',
            'background':'main_background',
            'year':datetime.now().year,
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
        }
        )