from django.shortcuts import render
from .models import Product


def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })


def product_list(request):

    search = request.GET.get('search')
    status = request.GET.get('status')
    products = Product.objects.all()

    if search:

        products = products.filter(
            name__icontains=search
        )

    if status:

        products = products.filter(
            status=status
        )

    context = {
        'products': products
    }

    return render(
        request,
        'products/product_list.html',
        context
    )

def product_detail(request, id):

    product = Product.objects.get(id=id)

    context = {
        'product': product
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )