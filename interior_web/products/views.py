from django.shortcuts import render, get_object_or_404
from .models import Product
from orders.models import Order


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

    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.exclude(id=id)[:4]

    context = {
        'product': product,
        'related_products': related_products
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )

def custom_page(request):
    return render(
        request,
        'products/custom.html'
    )

def about(request):
    return render(
        request,
        'products/about.html'
    )

