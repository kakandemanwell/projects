from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vehicle, Driver, Maintenance


# Create your views here.

def index(request):
    vehicles = Vehicle.objects.all().values()
    template = loader.get_template('index.html')
    context = {'Vehicle' : vehicles,
               'Driver' : Driver,
    }
    return HttpResponse(template.render(context, request))
