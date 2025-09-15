from sqlalchemy import Column, Integer, String, DECIMAL
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    protein = Column(DECIMAL(10, 2), nullable=False)
    fat = Column(DECIMAL(10, 2), nullable=False)
    carbohydrates = Column(DECIMAL(10, 2), nullable=False)