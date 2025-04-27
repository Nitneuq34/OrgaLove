from django.contrib import admin
from django.urls import path, include
from evenements.views import home  # Importe la vue home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evenements/', include('evenements.urls')),
    path('', home, name='home'),  # URL pour la page d'accueil
]