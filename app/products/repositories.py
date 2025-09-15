from sqlalchemy.orm import Session
from .. import models
from . import schemas

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_name(self, name: str) -> models.Product | None:
        return self.db.query(models.Product).filter(models.Product.name == name).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[models.Product]:
        return self.db.query(models.Product).offset(skip).limit(limit).all()

    def create(self, product: schemas.ProductCreate) -> models.Product:
        db_product = models.Product(**product.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product