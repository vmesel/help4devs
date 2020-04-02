from django import forms
from django.conf import settings
from django.forms import ModelForm
from .models import Dev

class DevForm(ModelForm):
    class Meta:
        model = Dev
        fields = [
            "name",
            "job",
            "place",
            "email",
            "github",
            "linkedin",
        ]