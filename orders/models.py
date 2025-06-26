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

    def save(self, *args, **kwargs):
        # Só diminui o estoque se for uma nova Order
        if self.pk is None:
            if self.product.quantity >= self.quantity:
                self.product.quantity -= self.quantity
                self.product.save()
            else:
                raise ValueError(f"Estoque insuficiente de {self.product.name}.")
        super().save(*args, **kwargs)