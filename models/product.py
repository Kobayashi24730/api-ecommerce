from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: Optional[int]
    name: str
    price: float
    category: str
    images: List[str]
    description: Optional[str] = None
