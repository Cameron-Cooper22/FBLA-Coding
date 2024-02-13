from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Sponsor
from django.db.models import Q

class DetailsSearchView(DetailView):
  model = Sponsor
  template_name = 'details.html'

  def get_object(self):
    id = self.kwargs.get("id")
    return Sponsor.objects.get(id=id)
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.session.get('query', '')
        context['sponsor'] = self.get_object()
        return context


class HomePageView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        sort = self.request.GET.get("sort", "name")
        object_list = Sponsor.objects.order_by(sort)
        return object_list

class SearchResultsView(ListView):
    model = Sponsor
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        self.request.session['query'] = query
        self.request.session.modified = True
        object_list = Sponsor.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query) | Q(phonenumber__icontains=query) | Q(category__icontains=query)
        )
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q")
        return context