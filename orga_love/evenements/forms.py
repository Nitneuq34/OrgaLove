from django import forms
from django.contrib.auth.models import User
from .models import Evenement

class EvenementForm(forms.ModelForm):
    autres_participants = forms.CharField(label="Autres participants (séparés par des virgules)", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Evenement
        fields = ['titre', 'date', 'heure_debut', 'heure_fin', 'description', 'participants', 'lieu', 'type', 'autres_participants']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'heure_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'participants': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
            'autres_participants': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participants'].queryset = User.objects.filter(username__in=['ton_nom_utilisateur', 'le_nom_utilisateur_de_ton_copain'])