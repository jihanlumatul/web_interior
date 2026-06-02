from django.db import models
from products.models import Product

class Order(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

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
        return self.customer_name