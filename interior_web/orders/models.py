from django.db import models
from products.models import Product
from datetime import datetime

class Order(models.Model):

    order_code = models.CharField(
        max_length=20, 
        unique=True, 
        blank=True,
        null=True
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    STATUS_CHOICES = [
        ('pending', 'Pending Payment'),
        ('paid', 'Paid'), 
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
        ('delivery', 'Out for Delivery'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    furniture_type = models.CharField(max_length=150)

    description = models.TextField()

    reference_image = models.ImageField(
        upload_to='orders/',
        blank=True,
        null=True
    )

    payment_proof = models.ImageField(
        upload_to='payments/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_code
    
    def save(self, *args, **kwargs):

        if not self.order_code:

            year = datetime.now().year

            last_order_obj = Order.objects.order_by('-id').first()
            next_id = (last_order_obj.id + 1) if last_order_obj else 1

            self.order_code = (
                f"MKD-{year}-{next_id:04d}"
            )

        super().save(*args, **kwargs)