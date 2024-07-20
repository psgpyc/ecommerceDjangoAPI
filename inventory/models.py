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

    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    is_digital = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False) #sets to current datetime when the object is created / cant be updated
    updated_at = models.DateTimeField(auto_now=True, editable=False) #updates the field to current date/time everytime the object is saved
    stock_status = models.CharField(max_length=3, choices=STOCK_STATUS, default=IN_STOCK)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    seasonal_event = models.ForeignKey('SeasonalEvents', on_delete=models.SET_NULL, null=True, blank=True)

class ProductLine(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sku = models.UUIDField(default=uuid.uuid4, editable=False)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)

class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField(default=0)
    product_line = models.ForeignKey('ProductLine', on_delete=models.SET_NULL, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True) #self referencing f_key


class SeasonalEvents(models.Model):
    start_date = models.DateTimeField(unique=True)
    end_date = models.DateTimeField()
    name = models.CharField(max_length=255)
