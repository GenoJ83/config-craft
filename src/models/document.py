from pydantic import BaseModel
from typing import Dict, Any
class ConfigDocument(BaseModel):
    format: str
    data: Dict[str, Any]
