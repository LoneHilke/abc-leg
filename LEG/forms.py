from django import forms
from .models import Ekstra

class GætForm(forms.Form):
    gæt = forms.CharField(label="Hvad forestiller billedet?", max_length=50)

class EkstraForm(forms.ModelForm):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'Tilføj...'}))

  class Meta:
    model = Ekstra 
    fields = '__all__'