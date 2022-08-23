from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username'}))
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('username не співпадає')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Не правильний пароль')
            user = authenticate(password=password, username=username)
            if not user:
                raise forms.ValidationError('Аккаунт користувача неактивний')
        return super().clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username'}))
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введіть пароль'}))
    password2 = forms.CharField(
        label="password2",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Паролі не співпадають')
        return data['password2']
