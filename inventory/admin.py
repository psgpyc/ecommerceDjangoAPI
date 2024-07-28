from django.contrib import admin

from inventory.models import (
    Product,
    ProductLine,
    ProductImage,
    Category,
    SeasonalEvents,
    Attribute,
    AttributeValue,
    ProductType
    )



class ProductLineInline(admin.StackedInline):
    model = ProductLine
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]
    list_display = (
        "name",
        "category",
        "stock_status",
        "is_active"
    )
    list_filter = (
        "stock_status",
    )






admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(SeasonalEvents)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductType)