def filter_keys(data: dict, prefix: str):
    return {k: v for k, v in data.items() if k.startswith(prefix)}
