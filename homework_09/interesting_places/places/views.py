from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import City, Place

# Create your views here.
def index_view(request):
    if request.method == 'GET':
        places = Place.objects.all()
        return render(request, 'places/index.html', {'places': places})
    else:
        raise Http404

class PlacesListView(ListView):
    model = Place
    template_name = 'places/index.html'


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/detail.html'


class PlaceCreateView(CreateView):
    model = Place
    template_name = 'places/edit.html'
    success_url = '/'
    fields = '__all__'


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = 'places/edit.html'
    success_url = '/'
    fields = '__all__'


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = 'places/delete_confirm.html'
    success_url = '/'


def contact_view(request):
    return render(request, 'places/contact.html')
