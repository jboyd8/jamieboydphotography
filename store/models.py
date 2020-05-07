from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, default='Print')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField(default='https://image.flaticon.com/icons/svg/38/38645.svg')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
