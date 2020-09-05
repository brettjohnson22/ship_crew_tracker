from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import StarshipCreateForm
from django.forms import modelformset_factory

from .models import Starship, Crewman, ShipClass


class ShipIndex(generic.ListView):
    template_name = 'crew_tracker/ship_index.html'
    context_object_name = 'ship_list'

    def get_queryset(self):
        return Starship.obejcts.all()


class CreateShip(generic.CreateView):
    template_name = 'crew_tracker/ship_index.html'


def create_ship(request):
    if request.method == 'POST':
        form = StarshipCreateForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get('name', '')
            ship_class = request.POST.get('ship_class', '')
            ship_class_from_db = get_object_or_404(ShipClass, pk=ship_class)

        ship = Starship(name=name, ship_class=ship_class_from_db)
        ship.save()

        form = StarshipCreateForm()

        return render(request, 'crew_tracker/create_ship.html', {'form': form})
    else:
        form = StarshipCreateForm()
        return render(request, 'crew_tracker/create_ship.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")


def ship_index(request):
    return HttpResponse("Hello, world. You're at the ship index.")


# Create your views here.
