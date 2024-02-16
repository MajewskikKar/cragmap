from map.models import Site

# Get the model's metadata
model_meta = Site._meta

# Access foreign keys
for field in model_meta.fields:
    if field.is_relation and field.many_to_one:
        print(f"{field.name} is a foreign key to {field.related_model}")
