from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from trains.models import Train
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from trains.forms import TrainForm


def home(request, pk=None):
    # if pk:
    #     city = get_object_or_404(Train, id=pk)
    #     context = {'object': city}
    #     return render(request, 'trains/detail.html', context)
    qs = Train.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)


class TrainsDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Потяг було створенно"


class TrainsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Потяг було відредаговано"


class TrainsDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    #template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Потяг видаленно')
        return self.delete(request, *args, **kwargs)


class TrainsListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = TrainForm
    #     context['form'] = form
    #     return context
