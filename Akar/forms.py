from django import forms


class RegisterForm(forms.Form):
    usr_name = forms.CharField()