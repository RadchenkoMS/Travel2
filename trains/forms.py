from django import forms

from trains.models import Train

from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(
        label="Потяг",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ваш потяг'}))
    travel_time = forms.IntegerField(label="Час", widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Введіть ваш час'}))
    from_town = forms.ModelChoiceField(
        label='Місто відбуття',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))
    to_town = forms.ModelChoiceField(
        label='Місто прибуття',
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))

    class Meta:
        model = Train
        fields = ('__all__')
