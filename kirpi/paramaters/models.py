from django.db import models
from decimal import Decimal

# Create your models here.

class Price(models.Model):
    price = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Birim Fiyat")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Katildigi Tarih")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Guncellendigi Tarih")

    class Meta:
        verbose_name = "Birim Fiyat"
        verbose_name_plural = "Birim Fiyatlar"
    
    def __str__(self) -> str:
        return f"{self.price}"


# class ElectricMeter(models.Model):
#     serial_number = models.ForeignKey(
#         "trailers.Trailer",
#         on_delete=models.CASCADE,
#         null=True,
#         related_name="trailer_serial_number",
#         verbose_name="Seri Numarasi",
#     )
#     last_t0 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T0")
#     last_t1 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T1")
#     last_t2 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T2")
#     last_t3 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="Onceki T3")
#     last_date = models.DateTimeField(verbose_name="Onceki Tarih")
#     t0 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T0")
#     t1 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T1")
#     t2 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T2")
#     t3 = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="T3")
#     ri = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="ri")
#     rc = models.DecimalField(null=True, max_digits=12, decimal_places=4, default=Decimal("0"), verbose_name="rc")
#     price = models.DecimalField(null=True, max_digits=15, decimal_places=3, default=Decimal("0"), verbose_name="price")
#     date = models.DateTimeField(auto_now=True, verbose_name="Tarih")

#     class Meta:
#         verbose_name = "Elektrik Sayaci"
#         verbose_name_plural = "Elektrik Sayaclari"
    
#     def __str__(self) -> str:
#         return f"{self.serial_number.serial_number}"
