from django import forms
from django.contrib.auth import get_user_model

USER = get_user_model()


class RegisterForm(forms.Form):
    usr_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={"placeholder": "نام کاربری"}))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={"placeholder": "ایمیل"}))
    passwd = forms.CharField(min_length=8, label="", widget=forms.PasswordInput(
        attrs={'placeholder': "رمز عبور"}))
    confirm_passwd = forms.CharField(min_length=8, label="", widget=forms.PasswordInput(
        attrs={"placeholder": "تایید رمز عبور"}))

    def clean(self):
        data = self.cleaned_data
        PASSWD = self.cleaned_data.get('passwd')
        USR_NAME = self.cleaned_data.get("usr_name")
        EMAIL = self.cleaned_data.get("email")
        CONFIRM_PASSWD = self.cleaned_data.get('confirm_passwd')

        if PASSWD != CONFIRM_PASSWD:
            raise forms.ValidationError("رمز و تایید رمز عبور یکی نیستند")

        passwd_qs = USER.objects.filter(username=USR_NAME)
        if passwd_qs.exists():
            raise forms.ValidationError(
                "نام کاربری قبلا استفاده شده است لطفا نام کاربری دیگری انتخاب کنید")

        email_qs = USER.objects.filter(email=EMAIL)
        if email_qs.exists():
            raise forms.ValidationError("ایمیل وارد شده قبل اسفاده شده است شما می‌توانید حساب کاربری خود را در لینک زیر باز یابی کیند")

        return USR_NAME
        return data
        return EMAIL
        
class LoginForm(forms.Form):
    usr_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "نام کاربری"}))
    passwd = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "رمز عبور"}))
