from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import StaffAuth

# # Login Form 

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

class StaffAuthCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model =StaffAuth
        fields = ('email',)

class StaffAuthChangeForm(UserChangeForm):

    class Meta:
        model =StaffAuth
        fields = ('email',)

