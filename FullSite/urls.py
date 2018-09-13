"""
Definition of urls for FullSite.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^photography$', app.views.photosMain, name='photos'),
    url(r'^design$', app.views.designMain, name='design'),
    url(r'^design/hardware$', app.views.designHardware, name='hardware'),
    url(r'^design/software$', app.views.designSoftware, name='software'),
    url(r'^photography/people$', app.views.photosPeople, name='people'),
    url(r'^photography/places$', app.views.photosPlaces, name='places'),
    url(r'^photography/weddings$', app.views.photosWeddings, name='weddings'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'template_name' : 'app/loggedoff.html'
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
