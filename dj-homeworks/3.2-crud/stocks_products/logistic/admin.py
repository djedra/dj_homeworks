from django.contrib import admin
from logistic.models import Stock, Product, StockProduct


# Register your models here.

class StockProductsInline(admin.TabularInline):
    model = Stock.products.through
    extra = 0


@admin.register(Product)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    inlines = [StockProductsInline]

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id','address')
    inlines = [StockProductsInline]


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock', 'product', 'quantity', 'price')