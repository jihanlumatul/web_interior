from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from products.models import Product
from .models import Order
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

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

    # HEADER

    p.setFont("Helvetica-Bold", 22)
    p.drawString(50, 800, "MKD DESIGN")

    p.setFont("Helvetica", 11)
    p.drawString(
        50,
        782,
        "Furniture & Interior Solution"
    )

    # GARIS HEADER

    p.line(50, 770, 550, 770)

    # JUDUL

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, 735, "ORDER RECEIPT")

    # INFO RECEIPT

    p.setFont("Helvetica", 11)

    p.drawString(
        400,
        735,
        f"Date: {datetime.now().strftime('%d/%m/%Y')}"
    )

    # GARIS

    p.line(50, 720, 550, 720)

    # DETAIL ORDER

    y = 680

    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Order Information")

    y -= 30

    p.setFont("Helvetica", 11)

    p.drawString(
        70,
        y,
        f"Order Code : {order.order_code}"
    )

    y -= 25

    p.drawString(
        70,
        y,
        f"Customer Name : {order.customer_name}"
    )

    y -= 25

    p.drawString(
        70,
        y,
        f"Email : {order.email}"
    )

    y -= 25

    p.drawString(
        70,
        y,
        f"Phone : {order.phone}"
    )

    y -= 25

    p.drawString(
        70,
        y,
        f"Address : {order.address}"
    )

    y-= 25

    p.drawString(
        70,
        y,
        f"Furniture : {order.furniture_type}"
    )

    y -= 25

    p.drawString(
        70,
        y,
        f"Status : {order.get_status_display()}"
    )

    y -= 25

    p.drawString(
        70,
        y,
        f"Order Date : {order.created_at.strftime('%d %B %Y')}"
    )

    # BOX

    p.rect(50, 450, 500, 260)

    # FOOTER

    p.line(50, 150, 550, 150)

    p.setFont("Helvetica-Oblique", 10)

    p.drawString(
        50,
        130,
        "This receipt serves as proof of order."
    )

    p.drawString(
        50,
        115,
        "Please keep this document for future reference."
    )

    p.drawString(
        50,
        80,
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