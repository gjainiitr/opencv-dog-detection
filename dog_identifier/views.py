from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from dog_identifier.detectDog import *
from .forms import *


def dog_classifier(request):
    if request.method == "POST":
        # load image on img
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, 'interface.html', {'form': form})
