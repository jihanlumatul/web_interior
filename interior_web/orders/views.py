from django.shortcuts import render, redirect
from .forms import OrderForm
from products.models import Product

def order_create(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('order_success')
        
    return render(
        request,
        'orders/order_create.html', 
        {'form': form}
            
    )

def order_product(request, product_id):

    product = Product.objects.get(id=product_id)

    form = OrderForm(
        initial={
            'furniture_type': product.name
        }
    )

    return render(
        request,
        'orders/order_create.html',
        {
            'form': form,
            'product': product
        }
    )

def order_success(request):
    return render(
        request,
        'orders/order_success.html'
    )