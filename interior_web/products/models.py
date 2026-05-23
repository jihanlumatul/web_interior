from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('ready', 'Ready'),
        ('sold', 'Sold'),
        ('custom', 'Custom'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return self.name
    