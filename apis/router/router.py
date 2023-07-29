from secrets import token_hex
from click import File
from fastapi import APIRouter, UploadFile
from fastapi import HTTPException, Form
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from model import Book, Response
from repositroy import BookRepo
import os
from fastapi import File, UploadFile, FastAPI
router = APIRouter()
import os
from fastapi import UploadFile

class Login(BaseModel):
    username: str
    password: str

class Book(BaseModel):
    id: int
    title: str
    author: str
# Sample student data
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
    try:
        book_dict = book.dict()
        books.append(book_dict)
        return HTTPException(status_code=200, detail="Book Successfully added") 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Read all books
@router.get("/books/")
async def read_books():
    return list(reversed(books))

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
            books.pop(idx)
            return  {"message" :"Successfully deleted " }
    raise HTTPException(status_code=404, detail="Book not found")   
 
@router.post("/upload-image")
async def create_upload_file(file: UploadFile):
    file_name = os.path.basename(file.filename)
    file_path = f"images/{file_name}"
    
    # Create the 'images' directory if it doesn't exist
    os.makedirs("images", exist_ok=True)

    with open(file_path, "wb") as f:
        contents = await file.read()  # Read the contents of the file
        f.write(contents)  # Write the contents to the file

    return {"message": f"File {file_name} uploaded successfully."}

@router.get("/download-image/{file_name}")
async def download_file(file_name: str):
    file_path = f"images/{file_name}"
    return FileResponse(file_path)
 




