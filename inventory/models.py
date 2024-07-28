import uuid
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    IN_STOCK = "IS"
    OUT_OF_STOCK = 'OOS'
    BACKORDERED = "BO"

    STOCK_STATUS = {
        IN_STOCK: 'In Stock',
        OUT_OF_STOCK: 'Out Of Stock',
        BACKORDERED: 'Back Ordered',
    }
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    description = models.TextField(null=True, blank=True)
    is_digital = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False) #sets to current datetime when the object is created / cant be updated
    updated_at = models.DateTimeField(auto_now=True, editable=False) #updates the field to current date/time everytime the object is saved
    stock_status = models.CharField(max_length=3, choices=STOCK_STATUS, default=IN_STOCK)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    seasonal_event = models.ForeignKey('SeasonalEvents', on_delete=models.SET_NULL, null=True, blank=True)
    product_type = models.ManyToManyField('ProductType', related_name='products', blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
        db_table = 'inventory_product'

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sku = models.UUIDField(default=uuid.uuid4, editable=False)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    attribute_value = models.ManyToManyField('AttributeValue', related_name='attributevalue', blank=True)

    class Meta:
        verbose_name = 'Product Line'
        verbose_name_plural = 'Product Lines'
        db_table = 'inventory_product_line'

    def __str__(self):
        return self.sku


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField(default=0)
    product_line = models.ForeignKey('ProductLine', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        db_table = 'inventory_product_image'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True) #self referencing f_key
    level = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'inventory_category'

    def __str__(self):
        return self.name

class SeasonalEvents(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Seasonal Event'
        verbose_name_plural = 'Seasonal Events'
        db_table = 'inventory_seasonal_events'

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=255)
    attribute = models.ForeignKey('Attribute', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Attribute Value'
        verbose_name_plural = 'Attribute Values'
        db_table = 'inventory_attribute_value'

    def __str__(self):
        return f"{self.attribute_value}-{self.attribute.name}"


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        db_table = 'inventory_attribute'

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'
        db_table = 'inventory_product_type'

    def __str__(self):
        return self.name