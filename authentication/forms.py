from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
    
    )
from django.forms import widgets

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 
                  'password1', 
                  'password2', 
                  'email', 
                  'first_name', 
                  'last_name'
                  )

class AccountForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
           'username',
           'first_name',
           'last_name',
           'email'
        )

        widgets = {
            'username' : forms.TextInput(
                attrs = 
                    {
                    'class' : 'form-control',
                    }
                
            ),
            'first_name' : forms.TextInput(
                attrs = 
                    {
                    'class' : 'form-control', 
                    'required' : ''
                    }
                ),
            'last_name' : forms.TextInput(
                attrs = 
                    {
                    'class' : 'form-control', 
                    'required' : ''
                    }
                ),
            'email' : forms.EmailInput(
                attrs = 
                    {
                    'class' : 'form-control', 
                    'required' : ''
                    }
                )
        }