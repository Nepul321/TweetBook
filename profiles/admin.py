from django.contrib import admin
from .models import (
    Profile
)

def register(model):
    admin.site.register(model)

register(Profile)