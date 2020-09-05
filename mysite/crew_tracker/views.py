from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import StarshipCreateForm, CrewmanCreateForm
from django.forms import modelformset_factory

from .models import Starship, Crewman, ShipClass, Rank, Department


class ShipIndex(generic.ListView):
    template_name = 'crew_tracker/ship_index.html'
    context_object_name = 'ship_list'

    def get_queryset(self):
        return Starship.objects.all()


class ShipDetails(generic.DetailView):
    model = Starship

    context_object_name = 'ship'
    template_name = 'crew_tracker/ship_details.html'


def create_ship(request):
    if request.method == 'POST':
        form = StarshipCreateForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get('name', '')
            ship_class = request.POST.get('ship_class', '')
            ship_class_from_db = get_object_or_404(ShipClass, pk=ship_class)

        ship = Starship(name=name, ship_class=ship_class_from_db)
        ship.save()

        return HttpResponseRedirect(reverse('crew_tracker:ship_index'))

    else:
        form = StarshipCreateForm()
        return render(request, 'crew_tracker/create_ship.html', {'form': form})


def create_crewman(request):
    if request.method == 'POST':
        form = CrewmanCreateForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get('name', '')
            rank = request.POST.get('rank', '')
            dept = request.POST.get('dept', '')
            ship_assignment = request.POST.get('ship_assignment', '')
            position = request.POST.get('position', '')

            rank_from_db = get_object_or_404(Rank, pk=rank)
            dept_from_db = get_object_or_404(Department, pk=dept)
            ship_from_db = get_object_or_404(Starship, pk=ship_assignment)

            crew = Crewman(name=name, rank=rank_from_db, dept=dept_from_db, ship_assignment=ship_from_db, position=position)
            crew.save()

            form = CrewmanCreateForm()

            return render(request, 'crew_tracker/create_crewman.html', {'form': form})

    else:
        form = CrewmanCreateForm()
        return render(request, 'crew_tracker/create_crewman.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world. You're at the main index.")


def ship_index(request):
    return HttpResponse("Hello, world. You're at the ship index.")


# Create your views here.
