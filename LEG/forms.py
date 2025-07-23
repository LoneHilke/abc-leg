from django import forms

class GætForm(forms.Form):
    gæt = forms.CharField(label="Hvad forestiller billedet?", max_length=50)