from typing import Optional
from pydantic import BaseModel
import uuid
from datetime import datetime, date
from typing import List
from src.reviews.schemas import ReviewModel


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    genre: str
    price: int
    published_date: date
    inStock: bool
    created_at: datetime
    updated_at: datetime
    
class BookDetailModel(Book):
    reviews: List[ReviewModel]

class BookCreateModel(BaseModel):
    title: str
    author: str
    genre: str
    published_date: date
    price: int
    inStock: bool

class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    published_date: Optional[date] = None
    price: Optional[int] = None
    inStock: Optional[bool] = None
