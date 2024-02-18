
from .models import Crag
from django import forms

class CragNameFilterForm(forms.Form):
    nazwa = forms.CharField(label='Nazwa', required=False)
    rodzaj = forms.ChoiceField(choices=[('', '---------')] + list(Crag.rodzaj_choices), label='Rodzaj', required=False)
    wyceny = forms.ChoiceField(choices=[('', '---------')] + list(Crag.wyceny_choices), label='Wyceny', required=False)
    skala = forms.ChoiceField(choices=[('', '---------')] + list(Crag.skala_choices), label='Rodzaj skały', required=False)
    ilosc_drog = forms.ChoiceField(choices=[('', '---------')] + list(Crag.ilosc_drog_choices), label='Ilość dróg', required=False)
    wysokosc_min = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'od', 'style': 'width: 50px;'}), label='Wysokość od', required=False)
    wysokosc_max = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'do', 'style': 'width: 50px;'}),label='Wysokość do', required=False)
    wiek_skal = forms.CharField(label='Wiek skał', required=False)
    facja = forms.CharField(label='Facja', required=False)
