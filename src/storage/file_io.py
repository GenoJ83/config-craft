def write_file_safe(path: str, content: str):
    with open(path, 'w') as f: f.write(content)
