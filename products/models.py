from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=5,decimal_places=2)
  quantity = models.PositiveIntegerField()

  def __str__(self):
    return self.name

  def available(self):
    return self.quantity > 0

  def unavailable(self):
    return not self.available
