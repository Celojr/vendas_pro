from django.db import models
from products.models import Product

class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.product.name} ({self.quantity}x)"

  def total_price(self):
    return self.quantity * self.product.price