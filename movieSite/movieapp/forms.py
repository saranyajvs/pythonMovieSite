from django import forms
from .models import Movie


class movieEditForm(forms.ModelForm):
    class Meta: # meta class should be same format, model and fileds
        model = Movie
        # fields = ['name', 'desc', 'year', 'image']
        fields = [ 'desc', 'year', 'image']

