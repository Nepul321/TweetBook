from django import forms
from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'location', 'bio')

        widgets = {
            'location' : forms.TextInput(attrs={'class' : 'form-control'}),
            'bio' : forms.Textarea(attrs={'class' : 'form-control'}),
        }