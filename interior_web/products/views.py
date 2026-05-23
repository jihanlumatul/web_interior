from django.shortcuts import render
from .models import Product


def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })


def product_list(request):

    search = request.GET.get('search')

    if search:

        products = Product.objects.filter(
            name__icontains=search
        )

    else:

        products = Product.objects.all()

    context = {
        'products': products
    }

    return render(
        request,
        'products/product_list.html',
        context
    )