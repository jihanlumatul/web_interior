from django.db import models

class Gallery(models.Model):

    CATEGORY_CHOICES = [

        ('livingroom', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('office', 'Office'),
        ('cafe', 'Cafe'),
    ]

    title = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='gallery/'
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):

        return self.title