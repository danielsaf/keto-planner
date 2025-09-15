from pydantic import BaseModel
from decimal import Decimal

# Basic product model
class ProductBase(BaseModel):
    name: str
    protein: Decimal
    fat: Decimal
    carbohydrates: Decimal

# Model used when creating a new product
class ProductCreate(ProductBase):
    pass

# Model used when reading a product from the database (also contains ID)
class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True