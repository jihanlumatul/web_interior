from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('product/<int:product_id>/', views.order_product, name='order_product'),
    path('payment/<int:order_id>/', views.payment_upload, name='payment_upload'),
    path('receipt/<int:order_id>/', views.receipt, name='receipt'),
    path('download-receipt/<int:order_id>/', views.download_receipt, name='download_receipt'),
    path('track-order/', views.track_order, name='track_order'),
]
