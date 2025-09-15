from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas
from .repositories import ProductRepository
from .services import ProductService
from ..core.database import SessionLocal

router = APIRouter()

# --- New dependency injection system ---

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_product_repository(db: Session = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db=db)

def get_product_service(
        repo: ProductRepository = Depends(get_product_repository)
) -> ProductService:
    return ProductService(product_repo=repo)


# --- Endpoints now using the service ---

@router.post("/", response_model=schemas.Product, status_code=201)
def create_new_product(
        product: schemas.ProductCreate,
        service: ProductService = Depends(get_product_service)
):
    try:
        return service.create_new_product(product_data=product)
    except HTTPException as e:
        raise e

@router.get("/", response_model=List[schemas.Product])
def read_products(
        skip: int = 0,
        limit: int = 100,
        service: ProductService = Depends(get_product_service)
):
    return service.get_all_products(skip=skip, limit=limit)