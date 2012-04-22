from django.views.generic import ListView, DetailView

from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Planet, SolarSystem 
from CompletePlanet import CompletePlanet

def complete_planet(request):
    planet_list = []

    # get list of solar systems which have distance !+ None
    systems = SolarSystem.objects.filter(distance__isnull=False)

    for system in systems:
    # For each system, find the list of planents
        planets = Planet.objects.filter(solar_system_id=system.id, radius__isnull=False)

        for planet in planets:
    # pass planet and system to custom object
            cplanet = CompletePlanet(planet, system)
            planet_list.append(cplanet)

    # get a list of CompletePlanet and pass it to view


    return HttpResponse(render_to_response('planets.html', {"planet_list": planet_list}))

class SystemMixin(object):
    model = SolarSystem
    def get_queryset(self):
        return super(SystemMixin, self).get_queryset().filter(radius__isnull=False)


class PlanetMixin(object):
    model = Planet
    def get_queryset(self):
        return super(PlanetMixin, self).get_queryset().filter(
                solar_system__radius__isnull=False,
                radius__isnull=False)


class SystemList(SystemMixin, ListView):
    pass


class SystemDetail(SystemMixin, DetailView):
    def get_context_data(self, **kwargs):
        data = super(SystemDetail, self).get_context_data(**kwargs)
        data.update({'planets': Planet.objects.filter(solar_system=self.object, radius__isnull=False)})
        return data

class PlanetList(PlanetMixin, ListView):
    pass

class PlanetDetail(PlanetMixin, DetailView):
    pass
