from django.contrib.admin import ModelAdmin, register

from kirpi.trailers.models import Trailer

# Register your models here.

@register(Trailer)
class TrailerAdmin(ModelAdmin):
    list_display = [
        "id",
        "serial_number",
        "last_t0",
        "last_t1",
        "last_t2",
        "last_t3",
        "last_ri",
        "last_rc",
        "t0",
        "t1",
        "t2",
        "t3",
        "ri",
        "rc",
        "price",
        "last_date",
        "date",
    ]
    readonly_fields = ["id", "last_date", "date"]