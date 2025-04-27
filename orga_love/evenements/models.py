from django.db import models
from django.contrib.auth.models import User

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    date = models.DateField()
    heure_debut = models.TimeField(null=True, blank=True)
    heure_fin = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participations')
    lieu = models.CharField(max_length=200, null=True, blank=True)
    rappel = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=[
        ('anniversaire', 'Anniversaire'),
        ('sortie', 'Sortie'),
        ('rdv_medical', 'Rendez-vous médical'),
        ('autre', 'Autre'),
    ], default='autre')

    def __str__(self):
        return self.titre