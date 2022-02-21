from django import forms
from .models import *
from django.db import models
from django.forms import fields


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


