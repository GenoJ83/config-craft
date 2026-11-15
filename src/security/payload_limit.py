def check_payload_size(raw: str, max_mb: int = 10):
    if len(raw) > max_mb * 1024 * 1024: raise ValueError('Config payload exceeds memory threshold')
