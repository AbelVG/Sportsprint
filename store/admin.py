from django.contrib import admin
from .models import Cloth, Quote


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "created_at")
