from django.contrib.admin import ModelAdmin, register

from kirpi.paramaters.models import Price

# Register your models here.

@register(Price)
class PriceAdmin(ModelAdmin):
    list_display = [
        "id",
        "price",
        "updated_at",
    ]
    readonly_fields = ["id", "updated_at"]
