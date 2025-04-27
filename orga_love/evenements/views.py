from django.shortcuts import render, redirect
from .models import Evenement
from .forms import EvenementForm


def liste_evenements(request):
    evenements = Evenement.objects.all().order_by('date')
    context = {'evenements': evenements}
    return render(request, 'evenements/liste_evenements.html', context)

def detail_evenement(request, evenement_id):
    evenement = Evenement.objects.get(pk=evenement_id)
    context = {'evenement': evenement}
    return render(request, 'evenements/detail_evenement.html', context)


def ajouter_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evenements:liste')  # Redirige vers la liste des événements après l'ajout
    else:
        form = EvenementForm()
    context = {'form': form}
    return render(request, 'evenements/ajouter_evenement.html', context)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')