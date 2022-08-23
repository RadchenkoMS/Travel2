from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from routes.forms import RouteForm
from routes.utils import route_finder
import pdb
from trains.models import Train
from cities.models import City
from routes.forms import RouteModelForm
from routes.models import Route


def home(request):
    form = RouteForm
    return render(request, 'routes/home.html', {'form': form})


def search_route(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = route_finder(request, form)
            except ValueError as error:
                messages.error(request, error)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        messages.error(request, "Поля не повині бути пустими")

@login_required
def add_route(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_town_id = int(data['from_city'])
            to_town_id = int(data['to_city'])
            trains = data['trains'].split(',')
            train_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(
                id__in=train_lst).select_related(
                'from_town', 'to_town')
            cities = City.objects.filter(
                id__in=[from_town_id, to_town_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_town': cities[from_town_id],
                    'to_town': cities[to_town_id],
                    'travel_time': total_time,
                    'trains': qs
                }
            )
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, "Неможливо зберегти маршрут")
        return redirect('/')

@login_required
def save_route(request):
    if request.method == "POST":
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Маршрут було успішно збережено")
            return redirect('/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, "Неможливо зберегти маршрут")
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 5
    model = Route
    template_name = 'routes/list.html'


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RoutesDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    #template_name = 'trains/delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Маршрут видаленно')
        return self.delete(request, *args, **kwargs)
