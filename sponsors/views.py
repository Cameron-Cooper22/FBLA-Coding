from django.http import HttpResponse
from django.template import loader
from .models import Sponsor

def sponsors(request):
    mysponsors = Sponsor.objects.all().values()
    template = loader.get_template('all_sponsors.html')
    context = {
        'mysponsors': mysponsors,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mysponsor = Sponsor.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mysponsor': mysponsor,
  }
  return HttpResponse(template.render(context, request))