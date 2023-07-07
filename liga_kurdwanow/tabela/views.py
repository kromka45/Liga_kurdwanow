from django.http import HttpResponse
from django.template import loader
from .models import Zespol

from django.shortcuts import render






def punkty():
  data = Zespol.objects.all()
  for i in data:
    # ... do stuff
    # i.update(field="value")
    i.punkty = (i.zwyciestwa * 3) + (i.remisy * 1) + (i.porazki * 0)
    i.save()


def bilans():
  data = Zespol.objects.all()
  for i in data:
    i.bilans = i.b_zdobyte - i.b_stracone
    i.save()

def index(request):


  punkty()
  bilans()
  r=0
  zespoly = Zespol.objects.order_by('-punkty')
  template = loader.get_template('tabela.html')
  context = {
    'zespoly': zespoly,
    'r':r,
  }
  return HttpResponse(template.render(context, request))


def liga(request):



  druzyny = Zespol.objects.all()
  punkty=druzyny('')
  liga_ptk  = Zespol.objects.order_by(punkty)

  context = {'liga_pkt': liga_ptk}

  return render(request, 'Blog/toys.html', context)

