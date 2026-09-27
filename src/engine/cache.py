class SchemaCache:
    _schemas = {}
    @classmethod
    def get(cls, uri): return cls._schemas.get(uri)
    @classmethod
    def set(cls, uri, s): cls._schemas[uri] = s
