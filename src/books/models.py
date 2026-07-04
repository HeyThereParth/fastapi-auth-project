from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import Optional
import uuid 


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str  
    author: str 
    genre: str
    price: int 
    published_date: datetime
    language: Optional[str]
    page_count: Optional[int]
    user_uid: Optional[uuid.UUID] = Field(default=None,foreign_key="users.uid")
    inStock: bool
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    
    
    def __repr__(self):
        return f"<Book {self.title}>"