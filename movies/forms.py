  
from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude=['']

class AvailForm(forms.ModelForm):
    class Meta:
        model = Available
        exclude=['']