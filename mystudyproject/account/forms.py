from django import forms
from django.contrib.auth.models import User
from .models import UserAdded, UserInfo

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm): #ModelForm 在需要改库的情况下使用.
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password2", widget=forms.PasswordInput)

    class Meta: #注意此处大写
        model = User
        fields = ("username", "email")

    def clean_password2(self): #'clean_%s' %name : is_valid()会调用这个函数并给cleaned_data[name]赋值
        cd = self.cleaned_data
        if cd['password'] != cd['password2'] :
            raise forms.ValidationError("password not match")
        return cd['password2']

class UserAddedForm(forms.ModelForm):
    class Meta:
        model = UserAdded
        fields = ("birth", "phone")

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "address", "company", "profession", "aboutme")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)