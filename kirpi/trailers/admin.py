from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from kirpi.trailers.models import Trailer

# Register your models here.

@register(Trailer)
class TrailerAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
    ]
    readonly_fields = ["id", "created_at"]