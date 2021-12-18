from django.contrib import admin
from .models import (
    Comment,
    Reply,
    SubReply
)

def registerModels(models):
    for model in models:
        admin.site.register(model)

registerModels([Comment, Reply, SubReply])