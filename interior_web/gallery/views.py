from django.shortcuts import render
from .models import Gallery

def gallery_page(request):

    galleries = Gallery.objects.all()
    category = request.GET.get('category')

    if category:
        galleries = galleries.filter(category=category)

    context = {
        'galleries': galleries
    }

    return render(
        request,
        'gallery/gallery.html',
        context
    )