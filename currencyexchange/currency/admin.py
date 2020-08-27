from django.contrib import admin

# Register your models here.
from currency import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Rate)
class RateAdmin(admin.ModelAdmin):
    pass