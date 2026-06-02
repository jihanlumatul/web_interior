from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =(
        'customer_name',
        'product',
        'phone',
        'furniture_type',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'furniture_type'
    )

    search_fields = (
        'customer_name',
        'phone',
    )