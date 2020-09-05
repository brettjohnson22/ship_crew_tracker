from django import forms
from . import models


class StarshipCreateForm(forms.ModelForm):
    class Meta:
        model = models.Starship
        fields = "__all__"


class CrewmanCreateForm(forms.ModelForm):
    class Meta:
        model = models.Crewman
        fields = "__all__"
