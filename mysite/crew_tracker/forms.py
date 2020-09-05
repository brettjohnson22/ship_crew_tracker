from django import forms
from . import models


class StarshipCreateForm(forms.ModelForm):
    class Meta:
        model = models.Starship
        fields = "__all__"
