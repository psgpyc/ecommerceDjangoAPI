from django.shortcuts import render
from django.db import transaction, IntegrityError
from inventory.models import Product, ProductInventory, Brand, ProductType, Stock

def test_atomic_transaction(requests):

    p13inch, created = Product.objects.get_or_create(web_id="1233",
                                slug="product-1",
                                name="ipad pro 13 inch",
                                description="a tengu sento product")
    brand, created = Brand.objects.get_or_create(brand_id=11111, name='Apple x')

    ptype, created = ProductType.objects.get_or_create(name="ipad")
    try:
        with transaction.atomic():
            pi = ProductInventory.objects.create(sku="0011111", upc="00111", product_type=ptype, product=p13inch, brand=brand,
                                                 retail_price=110.00, store_price=110.00, sale_price=110.00, weight=1100)

            s = Stock.objects.create(product_inventory=pi, units=1000)
    except IntegrityError:
        return render(requests, 'index.html', {'name':'Integrity Error'})


    return render(requests, 'index.html', {'name':[pi.sku, s.product_inventory.sku]})