from fastapi import HTTPException, status
from . import schemas
from .repositories import ProductRepository

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def get_all_products(self, skip: int = 0, limit: int = 100):
        return self.product_repo.get_all(skip=skip, limit=limit)

    def create_new_product(self, product_data: schemas.ProductCreate):
        # This is business logic: we do not allow duplicate product names.
        existing_product = self.product_repo.get_by_name(name=product_data.name)
        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product with this name already exists."
            )

        # If everything is OK, pass the data to the repository for saving.
        return self.product_repo.create(product=product_data)