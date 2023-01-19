from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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
    newRec.m_lname = request.POST.get('f_lname')
    newRec.m_fname = request.POST.get('f_fname')
    newRec.save()
    return HttpResponseRedirect("/")
    # return HttpResponse('Данные записаны...')

def delete(request, id):
    try:
        person = Clan.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Clan.DoesNotExist:
        return HttpResponseNotFound("<h2>Нет такого клиента</h2>")

def edit(request, id):
    person = Clan.objects.get(id=id)
    if request.method == "POST":
        person.m_lname = request.POST.get("f_name")
        person.m_fname = request.POST.get("l_name")
        person.save()
        return HttpResponseRedirect('/')
    else:
        # person = Clan.objects.get(id=id)
        return render(request, "edit.html", {"person": person})


