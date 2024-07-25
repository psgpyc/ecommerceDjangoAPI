import pytest
from django.db import  models
from inventory.models import Category, Product, SeasonalEvents, ProductType, ProductLine, AttributeValue, ProductImage, Attribute


# Confirm the presence of required table within in the database schema
@pytest.mark.model
def test_model_structure_table_exists():
    try:
        from inventory.models import Category
        from inventory.models import Product
        from inventory.models import SeasonalEvents
        from inventory.models import ProductType
        from inventory.models import ProductLine
        from inventory.models import ProductImage
        from inventory.models import Attribute
        from inventory.models import AttributeValue

    except ImportError:
        assert False
    else:
        assert True

@pytest.mark.parametrize(
    "model, field_name, expected_type",
    [
        (Category,"id", models.AutoField),
        (Category,"name", models.CharField),
        (Category,"slug", models.SlugField),
        (Category,"is_active", models.BooleanField),
        (Category,"level", models.IntegerField),
        (Category,"parent_category", models.ForeignKey),
        (Product, "id", models.BigAutoField),
        (Product, "name", models.CharField),
        (Product, "slug", models.SlugField),
        (Product, "description", models.TextField),
        (Product, "is_digital", models.BooleanField),
        (Product, "created_at", models.DateTimeField),
        (Product, "updated_at", models.DateField),
        (Product, "is_active", models.BooleanField),
        (Product, "stock_status", models.CharField),

        (SeasonalEvents, "id", models.BigAutoField),
        (SeasonalEvents, "start_date", models.DateTimeField),
        (SeasonalEvents, "end_date", models.DateTimeField),
        (SeasonalEvents, "name", models.CharField),

        (ProductLine, "price", models.DecimalField),
        (ProductLine, "sku", models.UUIDField),
        (ProductLine, "stock_qty", models.IntegerField),
        (ProductLine, "is_active", models.BooleanField),
        (ProductLine, "order", models.IntegerField),
        (ProductLine, "weight", models.FloatField),

        (ProductImage, "name", models.CharField),
        (ProductImage, "alternative_text", models.CharField),
        (ProductImage, "url", models.ImageField),
        (ProductImage, "order", models.IntegerField),

        (ProductType, "name", models.CharField),

        (Attribute, "name", models.CharField),
        (Attribute, "description", models.TextField),

        (AttributeValue, "attribute_value", models.CharField)


    ],
) 
def test_model_structure_column_data_types(model, field_name, expected_type):
    print('coming through........................................')
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have {field_name} field"

    field = model._meta.get_field(field_name)
    assert isinstance(
        field, expected_type
    )

# Ensure the accurate number of columns per table
@pytest.mark.parametrize(
        "model, expected_field_count",
        [
            (Product, 11),
            (ProductLine, 8),
            (ProductImage, 6),
            (Category, 6),
            (SeasonalEvents, 4),
            (AttributeValue, 3),
            (Attribute, 3),
            (ProductType, 3)

        ]
)
def test_model_structure(model, expected_field_count):
    print(model._meta.fields)
    field_count = len(model._meta.fields) 
    assert field_count == expected_field_count 

# Ensure that column relationships are correctly defined

@pytest.mark.parametrize(
    "model, field_name, expected_type, related_model, on_delete_behaviour, allow_null, allow_blank",
    [
        (Category,
         "parent_category",
         models.ForeignKey,
         Category,
         models.SET_NULL,
         True,
         True),
         (Product, "category", models.ForeignKey, Category, models.SET_NULL, True, True),
         (Product, "seasonal_event", models.ForeignKey, SeasonalEvents, models.SET_NULL, True, True),
         (Product, "product_type", models.ManyToManyField, ProductType, None, True, True),

         (ProductLine, "product", models.ForeignKey, Product, models.SET_NULL, True, True),
         (ProductLine, "attribute_value", models.ManyToManyField, AttributeValue, None, False, True),

         (ProductImage, "product_line", models.ForeignKey, ProductLine, models.SET_NULL, True, True ),

         (ProductType, "parent", models.ForeignKey, ProductType, models.CASCADE, True, True ),

         (AttributeValue, "attribute", models.ForeignKey, Attribute, models.SET_NULL, True, True)


         
        

    ]
)
def test_model_structure_relationship(model, field_name, expected_type, related_model, on_delete_behaviour, allow_null, allow_blank):
    assert hasattr(model, field_name)
    field = model._meta.get_field(field_name)
    assert isinstance(field, expected_type)
    assert (
        field.related_model == related_model
    )
    assert (
        field.remote_field.on_delete == on_delete_behaviour
    )
    assert (
        field.null == allow_null
    )
    assert (
            field.blank == allow_blank
    )

# verify nullable or not nullable filed

@pytest.mark.parametrize(
    "model, field_name, nullable_constraint", 
    [
        (Category, "id", False),
        (Category, "name", False),
        (Category, "slug", False),
        (Category, "is_active", False),
        (Category, "level", False),

        (Product, "id", False),
        (Product, "name", False),
        (Product, "slug", False),
        (Product, "description", True),
        (Product, "is_digital", False),
        (Product, "created_at", False),
        (Product, "updated_at", False),
        (Product, "is_active", False),
        (Product, "stock_status", False),

        (SeasonalEvents, "start_date", False),
        (SeasonalEvents, "end_date", False),
        (SeasonalEvents, "name", False),

        (ProductLine, "price", False),
        (ProductLine, "sku", False),
        (ProductLine, "stock_qty", False),
        (ProductLine, "is_active", False),
        (ProductLine, "order", False),
        (ProductLine, "weight", False),

        (ProductImage, "name", False),
        (ProductImage, "alternative_text", False),
        (ProductImage, "url", False),
        (ProductImage, "order", False),

        (ProductType, "name", False),

        (Attribute, "name", False),
        (Attribute, "description", True),

        (AttributeValue, "attribute_value", False)





    ]
)
def test_model_structure_nullable_constraints(model, field_name, nullable_constraint):
    field = model._meta.get_field(field_name)
    assert (
        field.null == nullable_constraint
    )

# verify default values for relevent columns
@pytest.mark.parametrize(
    "model, field_name, expected_default_value",
    [
        (Category, "is_active", False ),

        
        (Product, "is_digital", False),
        (Product, "is_active", False),

        (ProductLine, "stock_qty", 0),
        (ProductLine, "is_active", False),
        (ProductLine, "order", 0),
        (ProductLine, "weight", 0),

        (ProductImage, "order", 0),
        
    ]
)
def test_model_structure_default_values(model, field_name, expected_default_value):
    field = model._meta.get_field(field_name)
    filed_default_value = field.default 
    assert (
        filed_default_value == expected_default_value
    ) 


# verify column lengths 

@pytest.mark.parametrize(
    "model, field_name, expected_length",
    [
        (Category, "name", 255),
        (Category, "slug", 255),

        (Product, "name", 255),
        (Product, "slug", 255),     
        (Product, "stock_status", 3),

       
        (SeasonalEvents, "name", 255),

        (ProductImage, "name", 100),
        (ProductImage, "alternative_text", 100),

        (ProductType, "name", 255),

        (Attribute, "name", 255),

        (AttributeValue, "attribute_value", 255)
        
    ]
)
def test_model_structure_column_length(model, field_name, expected_length):
    field = model._meta.get_field(field_name)
    assert ( field.max_length == expected_length)

@pytest.mark.parametrize(
    "model, field_name, expected_unique_constraint",
    [
        (Category, "name", True),
        (Category, "slug", True),
        (Category,  "is_active", False),
        (Category,  "parent_category", False),
        (Category, "level", False),

        (Product, "id", True),
        (Product, "name", True),
        (Product, "slug", True),
        (Product, "description", False),
        (Product, "is_digital", False),
        (Product, "created_at", False),
        (Product, "updated_at", False),
        (Product, "is_active", False),
        (Product, "stock_status", False),

        (SeasonalEvents, "id", True),
        (SeasonalEvents, "start_date", False),
        (SeasonalEvents, "end_date", False),
        (SeasonalEvents, "name", True),

        (ProductType, "name", False)

        
    ]
)
def test_model_structure_unique_constraint(model, field_name, expected_unique_constraint):
    field = model._meta.get_field(field_name)
    assert(
        field.unique == expected_unique_constraint
    )
