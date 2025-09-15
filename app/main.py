from fastapi import FastAPI
from . import models
from .core.database import engine
from .products import routes as product_routes

# Create all tables in the database. If the tables already exist, this will do nothing.
# For development mode.
models.Base.metadata.create_all(bind=engine)

# Initialization of the main FastAPI application instance.
# Adding a title and description is good practice for documentation.
app = FastAPI(
    title="Keto Medical Diet API",
    description="API for managing products and recipes in a ketogenic medical diet application.",
    version="1.0.0"
)

# Including the router with endpoints from the 'products' module.
# All paths from this router will have the "/products" prefix.
# In Swagger UI documentation, they will be grouped under the "Products" tag.
app.include_router(
    product_routes.router,
    prefix="/products",
    tags=["Products"]
)

# In the future, to add endpoints for recipes, just add these two lines:
# from .recipes import routes as recipe_routes
# app.include_router(recipe_routes.router, prefix="/recipes", tags=["Recipes"])


# Main endpoint, often used as a "health check" to verify if the API is running.
@app.get("/", tags=["Root"])
def read_root():
    """Returns a welcome message."""
    return {"message": "Welcome to the Keto Medical Recipes API!"}