from django.db import models
from decimal import Decimal

# Create your models here.

class Price(models.Model):
    price = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Birim Fiyat")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Son Guncelleme Tarihi")

    class Meta:
        verbose_name = "Birim Fiyat"
        verbose_name_plural = "Birim Fiyatlar"
    
    def __str__(self) -> str:
        return f"{self.price}"
