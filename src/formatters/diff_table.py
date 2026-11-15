def format_diff_table(diff: dict) -> str:
    return f"Added: {diff['added']}\nRemoved: {diff['removed']}"
