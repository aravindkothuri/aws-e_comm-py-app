from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Cloud E-Commerce API", version="1.0.0")

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

@app.get("/health")
def health_check():
    """Cloud readiness and liveness probe endpoint."""
    return {"status": "healthy", "environment": os.getenv("ENVIRONMENT", "production")}

@app.get("/api/products", response_model=list[Product])
def get_products():
    """Retrieve product catalog."""
    return [
        {"id": 1, "name": "Wireless Mechanical Keyboard", "price": 89.99, "stock": 45},
        {"id": 2, "name": "Ergonomic Office Chair", "price": 249.99, "stock": 12},
    ]

@app.post("/api/orders")
def create_order(product_id: int, quantity: int):
    """Process customer orders."""
    return {"message": "Order placed successfully", "product_id": product_id, "quantity": quantity}
