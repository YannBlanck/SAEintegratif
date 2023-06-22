from django.shortcuts import render
from .forms import stampForm
from . import models
from django.http import HttpResponseRedirect


def appindex(request):
    liste2 = list(models.stamp.objects.all())
    return render(request, 'SAEapplication/index.html', {"liste": liste2})


def appajout(request):
    form = stampForm()
    return render(request, "SAEapplication/ajout.html", {"form": form})


def apptraitement(request):
    lform = stampForm(request.POST)
    if lform.is_valid():
        stamp = lform.save()
        return HttpResponseRedirect("/SAEAPP")
    else:
        return render(request,"SAEapplication/ajout.html", {"form": lform})

def appaffiche(request, id):
    stamp = models.stamp.objects.get(pk=id)
    return render(request, "SAEapplication/affiche.html", {"stamp": stamp})


def appupdate(request, id):
    stampp = models.stamp.objects.get(pk=id)
    form = stampForm(stampp.eod())
    return render(request, "SAEapplication/ajout.html", {"form": form})


def appupdatetraitement(request, id):
    lform = stampForm(request.POST)
    if lform.is_valid():
        stampp = lform.save(commit=False)
        stampp.id = id  # modification de l'id de l'objet
        stampp.save()  # mise à jour dans la base puisque l'id du livre existe déja.
        return HttpResponseRedirect("/SAEAPP/")  # plutot que d'avoir un gabarit
    else:
        return render(request, "SAEapplication/ajout.html", {"lform": lform, "id": id})

def appdelete(request, id):
    stamp = models.stamp.objects.get(pk=id)
    stamp.delete()
    return HttpResponseRedirect('/SAEAPP/')
