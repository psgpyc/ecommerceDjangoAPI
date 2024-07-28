class InventoryRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == "inventory":
            return "inventory_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label  == "inventory":
            return "inventory_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label  == "inventory"
                and obj2._meta.app_label  == "inventory"
        ):
            return "inventory_db"
        return None

    def allow_migrate(self, app_label, db,  model_name=None, **hints):
        if app_label == "inventory":
            return "inventory_db"
        return None
