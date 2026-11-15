from jsonschema import validate
def validate_against_schema(data: dict, schema: dict) -> bool:
    validate(instance=data, schema=schema)
    return True
