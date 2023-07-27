from fastapi import APIRouter
from fastapi import HTTPException, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model import Book, Response
from repositroy import BookRepo

router = APIRouter()


class Login(BaseModel):
    username: str
    password: str

class Book(BaseModel):
    id: int
    title: str
    author: str
# Sample student data
students = [
    {
        "name": "John Doe",
        "age": 20,
        "image": "https://example.com/images/john.jpg"
    },
    {
        "name": "Jane Smith",
        "age": 21,
        "image": "https://example.com/images/jane.jpg"
    },
    # Add more student entries as needed
]

books = []
@router.post("/login")
async def login(request: Login ):
    if request.username == "kiran" and request.password == "Kiran@123":
        raise HTTPException(status_code=200, detail="Successfully logged")
    else:
        raise HTTPException(status_code=401, detail="Username or Password Incorrect")
# Create a book
@router.post("/books/" )
async def create_book(book: Book):
    book_dict = book.dict()
    books.append(book_dict)
    return book_dict

# Read all books
@router.get("/books/")
async def read_books():
    return books

# Read a book by ID
@router.get("/books/{book_id}" )
async def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Update a book
@router.put("/books/{book_id}" )
async def update_book(book_id: int, book: Book):
    for idx, stored_book in enumerate(books):
        if stored_book["id"] == book_id:
            stored_book.update(book.dict())
            return stored_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete a book
@router.delete("/books/{book_id}" )
async def delete_book(book_id: int):
    for idx, stored_book in enumerate(books):
        if stored_book["id"] == book_id:
            return books.pop(idx)
    raise HTTPException(status_code=404, detail="Book not found")   
# @router.get("/book/")
# async def get_all():
#     _bookList = await BookRepo.retrieve()
#     return Response(code=200, status="Ok", message="Success retrieve all data", result=_bookList).dict(exclude_none=True)


# @router.post("/book/create")
# async def create(book: Book):
#     await BookRepo.insert(book)
#     return Response(code=200, status="Ok", message="Success save data").dict(exclude_none=True)


# @router.get("/book/{id}")
# async def get_id(id: str):
#     _book =  BookRepo.retrieve_id(id)
#     return Response(code=200, status="Ok", message="Success retrieve data", result=_book).dict(exclude_none=True)


# @router.post("/book/update")
# async def update(book: Book):
#     BookRepo.update(book.id,book)
#     return Response(code=200, status="Ok", message="Success update data").dict(exclude_none=True)


# @router.delete("/book/{id}")
# async def delete(id: str):
#     BookRepo.delete(id)
#     return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
