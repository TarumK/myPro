from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormClan
from .models import Clan

# Create your views here.

def index(request):
    form = FormClan()
    request_all = Clan.objects.all()
    return render(request, "index.html", {'myForm' : form, 'request_all' : request_all })

def quest(request):
    # if request.method == "POST":
    newRec = Clan()
    newRec.m_fname = request.POST.get('f_fname')
    newRec.m_lname = request.POST.get('f_fname')
    newRec.save()
    return HttpResponse('Данные записаны...')

