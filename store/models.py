from django.db import models


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    items = models.TextField()  # simple JSON structure

    def __str__(self):
        return f"Quote {self.id}"
