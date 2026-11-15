from pydantic import BaseModel
class ConverterConfig(BaseModel):
    indent: int = 2
    sort_keys: bool = True
    allow_comments: bool = True
