from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import List, Optional
import uuid


class User(SQLModel, table=True):
    __tablename__ = 'users'
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    username : str
    email : str
    first_name : str
    last_name : str
    role: str = Field(sa_column = Column(
        pg.VARCHAR, nullable=False, server_default="user"
    ))
    is_verified : bool = Field(default=False)
    password_hash: str = Field(exclude=True)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: List["Book"] =Relationship(back_populates="user", sa_relationship_kwargs={'lazy':'selectin'})
    reviews: List["Review"] =Relationship(back_populates="user", sa_relationship_kwargs={'lazy':'selectin'})
    
    def __repr__(self):
        return f"<Book {self.username}>"
    
    



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
    language: Optional[str] = Field(default=None, nullable=True)
    page_count: Optional[int] = Field(default=None, nullable=True)  
    user_uid: Optional[uuid.UUID] = Field(default=None,foreign_key="users.uid")
    inStock: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    user: Optional["User"] =Relationship(back_populates="books")
    reviews: List["Review"] =Relationship(back_populates="book", sa_relationship_kwargs={'lazy':'selectin'})
    
    def __repr__(self):
        return f"<Book {self.title}>"
    
    
class Review(SQLModel, table=True):
    __tablename__ = "reviews"
    uid: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    
    rating: int = Field(lt=5)
    review_text: str
    user_uid: Optional[uuid.UUID] = Field(default=None,foreign_key="users.uid")
    book_uid: Optional[uuid.UUID] = Field(default=None,foreign_key="books.uid")
    inStock: Optional[bool]
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    user: Optional["User"] =Relationship(back_populates="reviews")
    book: Optional["Book"] =Relationship(back_populates="reviews")
    
    
    def __repr__(self):
        return f"<Review for {self.book_uid}> by user {self.user_uid}"
    
    
    