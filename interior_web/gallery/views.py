from django.shortcuts import render
from .models import Gallery

def gallery_page(request):

    galleries = Gallery.objects.all()
    context = {
        'galleries': galleries
    }

    return render(
        request,
        'gallery/gallery.html',
        context
    )