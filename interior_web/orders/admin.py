from django.contrib import admin
from .models import Order
from django.utils.html import format_html

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_code',
        'customer_name',
        'email',
        'phone',
        'furniture_type',
        'payment_preview',
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
        'order_code'
    )

    readonly_fields = (
        'payment_preview',
        'payment_proof',
        'order_code',
        'created_at'
    )

    def payment_preview(self, obj):

        if obj.payment_proof:
            return format_html(
                '<a href="{}" target="_blank">View Proof</a>',
                obj.payment_proof.url
            )

        return '-'

    payment_preview.short_description = 'Payment Proof'
