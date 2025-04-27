from django.urls import path
from . import views

app_name = 'evenements'

urlpatterns = [
    path('', views.liste_evenements, name='liste'),
    path('<int:evenement_id>/', views.detail_evenement, name='detail'),
    path('ajouter/', views.ajouter_evenement, name='ajouter'),  # Ajoute cette ligne
]