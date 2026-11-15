import json
def dump_json(data: dict, indent: int = 2) -> str:
    return json.dumps(data, indent=indent, sort_keys=True)
