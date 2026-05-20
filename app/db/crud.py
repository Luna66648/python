from sqlalchemy.orm import Session
from app.db import models

# ========== CRUD ДЛЯ КАТЕГОРИЙ ==========

def create_category(db: Session, title: str):
    category = models.Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def update_category(db: Session, category_id: int, title: str):
    category = get_category_by_id(db, category_id)
    if category:
        category.title = title
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category

# ========== CRUD ДЛЯ КНИГ ==========

def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_books_by_category(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data):
    book = get_book_by_id(db, book_id)
    if book:
        if hasattr(book_data, 'title') and book_data.title is not None:
            book.title = book_data.title
        if hasattr(book_data, 'description') and book_data.description is not None:
            book.description = book_data.description
        if hasattr(book_data, 'price') and book_data.price is not None:
            book.price = book_data.price
        if hasattr(book_data, 'url') and book_data.url is not None:
            book.url = book_data.url
        if hasattr(book_data, 'category_id') and book_data.category_id is not None:
            book.category_id = book_data.category_id
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book
