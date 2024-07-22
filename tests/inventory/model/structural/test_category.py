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


