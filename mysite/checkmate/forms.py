from django import forms
from .models import Diseases, Gender


class GenderForm(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = ['gender_disease', 'diseases']



