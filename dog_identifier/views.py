from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib import messages
from dog_identifier.detectDog import *
from .forms import *
import os


def dog_classifier(request):
    if request.method == "POST":
        # load image on img
        image = request.FILES['img']
        imageName = image.name

        path = default_storage.save('img.jpg', ContentFile(image.read()))
        img_path = os.path.join(settings.MEDIA_ROOT, path)
        res = dog_detector(img_path)
        os.remove(img_path)
        if res:
            return HttpResponse("A Dog", content_type='text/plain')
        else:
            return HttpResponse("Not a Dog", content_type='text/plain')


    form = ImageForm()

    return render(request, 'interface.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')