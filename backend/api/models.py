from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self) -> str:
        return self.title

    @property
    def sale_price(self):
        return round(float(self.price) * 0.75, 2)
