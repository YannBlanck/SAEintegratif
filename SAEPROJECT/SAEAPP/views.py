from django.shortcuts import render
from .forms import DoneForm
from . import models
from django.http import HttpResponseRedirect


def index(request):
    liste = list(models.Doone.objects.all())
    return render(request, 'SAEAPP/index.html', {"liste": liste})


def ajout(request):
    form = DoneForm()  # création d'un formulaire vide
    return render(request, "SAEAPP/ajout.html", {"form": form})


def traitement(request):
    lform = DoneForm(request.POST)
    if lform.is_valid():
        Done = lform.save()

        return HttpResponseRedirect("/SAEAPP")
    else:
        return render(request,"SAEAPP/ajout.html", {"form": lform})

def affiche(request, id):
    Done = models.Doone.objects.get(pk=id)  # méthode pour récupérer les données dans la base avec un id donnée
    return render(request, "SAEAPP/affiche.html", {"Done": Done})


def update(request, id):
    Donne = models.Doone.objects.get(pk=id)
    form = DoneForm(Donne.Doe())
    return render(request, "SAEAPP/ajout.html", {"form": form})


def updatetraitement(request, id):
    lform = DoneForm(request.POST)
    if lform.is_valid():
        Done = lform.save(commit=False)
        Done.id = id  # modification de l'id de l'objet
        Done.save()  # mise à jour dans la base puisque l'id du livre existe déja.
        return HttpResponseRedirect("/SAEAPP/")  # plutot que d'avoir un gabarit
    else:
        return render(request, "SAEAPP/ajout.html", {"lform": lform, "id": id})

def delete(request, id):
    Done = models.Doone.objects.get(pk=id)
    Done.delete()
    return HttpResponseRedirect('/SAEAPP/')
