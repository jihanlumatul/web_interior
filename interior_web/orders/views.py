from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from products.models import Product
from .models import Order
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def order_create(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            order = form.save()
            return redirect('payment_upload', order_id=order.id)
        
    return render(
        request,
        'orders/order_create.html', 
        {'form': form}
            
    )

def order_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        form = OrderForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            order = form.save(commit=False)
            order.product = product
            order.save()

            return redirect(
                'payment_upload',
                order_id=order.id
            )
        
        else:
            print(form.errors)

    else:

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

def payment_upload(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.payment_proof = request.FILES.get('payment_proof')
        order.status = 'paid'
        order.save()
        return redirect('receipt', order_id=order.id)
    
    return render(
        request,
        'orders/payment_upload.html',
        {
            'order': order
        }
    )

def receipt(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    return render(
        request,
        'orders/receipt.html', {
            'order': order
        }
    )

def download_receipt(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="receipt_{order.order_code}.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 18)
    p.drawString(100, 800, "MKD DESIGN")

    p.setFont("Helvetica", 12)

    p.drawString(100, 760, f"Order ID : {order.order_code}")
    p.drawString(100, 740, f"Customer : {order.customer_name}")
    p.drawString(100, 720, f"Phone : {order.phone}")
    p.drawString(100, 700, f"Furniture : {order.furniture_type}")
    p.drawString(100, 680, f"Status : {order.status}")

    p.drawString(
        100,
        640,
        "Thank you for choosing MKD Design."
    )

    p.showPage()
    p.save()

    return response


def track_order(request):
    order = None
    if request.method == 'POST':
        code = request.POST.get('order_code')
        try:
            order = Order.objects.get(order_code=code)
        except Order.DoesNotExist:
            order = None

    return render(
        request,
        'orders/track_order.html',
        {
            'order': order
        }
    )