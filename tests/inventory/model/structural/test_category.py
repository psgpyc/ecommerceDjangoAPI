import pytest
from django.db import  models
from inventory.models import Category
# Confirm the presence of required table within in the database schema


@pytest.mark.model
def test_model_structure_table_exists():
    try:
        from inventory.models import Category
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
        (Category,"parent_category", models.ForeignKey)
    ],
) 
def test_model_structure_column_data_types(model, field_name, expected_type):
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have {field_name} field"

    field = model._meta.get_field(field_name)
    assert isinstance(
        field, expected_type
    )