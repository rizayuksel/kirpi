from decimal import Decimal
from datetime import datetime
from django.db import models

# Create your models here.

class Trailer(models.Model):
    serial_number = models.CharField(max_length=15, null=True, verbose_name="Sayac Seri Numarasi")
    last_t0 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T0")
    last_t1 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T1")
    last_t2 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T2")
    last_t3 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T3")
    last_ri = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki RI")
    last_rc = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki RC")
    last_date = models.DateTimeField(default=datetime.now(), verbose_name="Onceki Tarih")
    t0 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T0")
    t1 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T1")
    t2 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T2")
    t3 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T3")
    ri = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="RI")
    rc = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="RC")
    price = models.DecimalField(null=True, max_digits=15, decimal_places=3, default=Decimal("0"), verbose_name="price")
    date = models.DateTimeField(auto_now=True, verbose_name="Tarih")

    class Meta:
        verbose_name = "Karavan"
        verbose_name_plural = "Karavanlar"
    
    def __str__(self) -> str:
        return f"{self.serial_number}"
    
