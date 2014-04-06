from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
# from trialshop.models import myUser
from django.forms import ModelForm

import re
# class UserForm(ModelForm):
# 	class Meta:
# 		model = myUser
# 		fields = '__all__'

   
    # class Meta:
    #     model = myUser
    #     widgets = {
    #     'password': forms.PasswordInput(),
    # }
class LoginForm(forms.Form):
	username = forms.CharField(label=("Username"), max_length=30)
	# username = forms.CharField(max_length=100)
	password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(render_value=False)
    )
# 	class Meta:
# 		model = User
	
	# password = forms.CharField(widget=forms.PasswordInput)
	
class SignupForm(forms.Form):

    first_name = forms.CharField(
        label=("first_name"),
        max_length=30,
        widget=forms.TextInput(),
        required=True
    )
    last_name = forms.CharField(
        label=("last_name"),
        max_length=30,
        widget=forms.TextInput(),
        required=True
    )
    username = forms.CharField(
        label=("Username"),
        max_length=30,
        widget=forms.TextInput(),
        required=True
    )
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(render_value=False),
        required=True
    )
    password_confirm = forms.CharField(
        label=("Password (again)"),
        widget=forms.PasswordInput(render_value=False),
        required=True
    )
    email = forms.EmailField(
        label=("Email"),
        widget=forms.TextInput(), required=True)

class quanti(forms.Form):

    Qunty = forms.CharField(
        label=("Qunty"),
        max_length=30,
        widget=forms.TextInput(),
        required=True
    )

