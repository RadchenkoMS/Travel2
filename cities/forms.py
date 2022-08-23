from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(
        label="Місто",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваше місто'}))

    class Meta:
        model = City
        fields = ('name',)
