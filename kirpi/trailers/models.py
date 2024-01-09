from django.db import models

# Create your models here.

class Trailer(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Karavan Ismi")
    is_active = models.BooleanField(default=True, verbose_name="Aktif Mi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Katildigi Tarih")

    class Meta:
        verbose_name = "Karavan"
        verbose_name_plural = "Karavanlar"
