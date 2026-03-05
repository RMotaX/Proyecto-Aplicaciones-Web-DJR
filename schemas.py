from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional, List

# --- SCHEMAS PARA CATEGORÍAS ---

class CategoryBase(BaseModel):
    category: str = Field(..., min_length=3, max_length=100)

class CategoryCreate(CategoryBase):
    pass # Se usa para el POST de categorías

class Category(CategoryBase):
    id_category: int
    
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS PARA PRODUCTOS ---

class ProductBase(BaseModel):
    product: str = Field(..., min_length=5, max_length=100)
    stock: int = Field(default=0, ge=0) # ge=0 evita stocks negativos
    price: float = Field(..., gt=0)     # gt=0 obliga a que el precio sea mayor a 0
    description: Optional[str] = Field(None, max_length=250)
    id_category: int
    date_exp: Optional[date] = None

class ProductCreate(ProductBase):
    # Aquí podrías agregar el campo de imagen si lo manejas como string (URL)
    image: Optional[str] = None
    pass

class Product(ProductBase):
    id_product: int
    image: Optional[str] = None
    
    # Esto permite que Pydantic lea los datos de SQLAlchemy (objetos) 
    # y los convierta a JSON automáticamente.
    model_config = ConfigDict(from_attributes=True)