from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('product/<int:product_id>/', views.order_product, name='order_product'),
    path('success/', views.order_success, name='order_success'),
]