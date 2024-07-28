# SQL migration code


**Add check empty constraint**
```sql
ALTER TABLE inventory_category
ADD CONSTRAINT inventory_category_chk_empty_name
CHECK (name IS NOT NULL AND name <> '');
```

**function and trigger to lowercase name filed**
```sql
CREATE OR REPLACE FUNCTION lowercase_name_trigger()
RETURNS TRIGGER AS $$
BEGIN
    NEW.name := LOWER(NEW.name);
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER category_lowercase_name_trigger
BEFORE INSERT OR UPDATE ON inventory_category 
FOR EACH ROW 
EXECUTE FUNCTION lowercase_name_trigger();
```
**Add slug constraint**
```sql
ALTER TABLE inventory_category
ADD CONSTRAINT inventory_category_chk_slug_format
CHECK (slug ~ '^[a-z0-9_-]+$' AND lower(slug) = slug);
```
