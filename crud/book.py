from sqlalchemy.orm import Session
from model import Book
from schemas import BookSchema


# Get All Book Data
def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


# Get book data by id
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


# Create book data
def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, description=book.description, price=book.price)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


# Remove book data by id
def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    if _book:
        db.delete(_book)
        db.commit()
    return _book


# Update book data by id
def update_book(db: Session, book_id: int, title: str, description: str, price: float):
    _book = get_book_by_id(db=db, book_id=book_id)
    if _book:
        _book.title = title
        _book.description = description
        _book.price = price
        db.commit()
        db.refresh(_book)
    return _book


