from django.contrib import admin

from inventory.models import (
    Product,
    ProductLine,
    ProductImage,
    Category,
    SeasonalEvents,
    Attribute,
    AttributeValue,
    ProductType)


admin.site.register(Product)
admin.site.register(ProductLine)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(SeasonalEvents)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductType)