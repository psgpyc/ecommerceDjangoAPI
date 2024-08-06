from inventory.models import Product, ProductInventory, Brand, ProductType, Stock


p1 = Product.objects.create(web_id="123", slug="product-1", name="ipad pro 11 inch", description="a tengu sento product")

b1 = Brand.objects.create(brand_id=1, name='Apple', nickname="tinku badi")

pt1 = ProductType.objects.create(name="ipad")

pi = ProductInventory.objects.create(sku="0011", upc="0011", product_type=pt1, product=p1, brand=b1, retail_price=10.00, store_price=10.00, sale_price=10.00, weight=100)

s = Stock.objects.create(product_inventory=pi, units=1000)