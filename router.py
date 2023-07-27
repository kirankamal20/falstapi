from fastapi import APIRouter
from fastapi import HTTPException, Form
from pydantic import BaseModel
from model import Book, Response
from repositroy import BookRepo

router = APIRouter()


class Login(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(request: Login ):
    if request.username == "kiran" and request. password == "Kiran@123":
        raise HTTPException(status_code=200, detail="Successfully logged")
    else:
        # Returning HTTPException with status code 401 (Unauthorized)
        raise HTTPException(status_code=401, detail="Username or Password Incorrect")

 
     
@router.get("/book/")
async def get_all():
    _bookList = await BookRepo.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=_bookList).dict(exclude_none=True)


@router.post("/book/create")
async def create(book: Book):
    await BookRepo.insert(book)
    return Response(code=200, status="Ok", message="Success save data").dict(exclude_none=True)


@router.get("/book/{id}")
async def get_id(id: str):
    _book =  BookRepo.retrieve_id(id)
    return Response(code=200, status="Ok", message="Success retrieve data", result=_book).dict(exclude_none=True)


@router.post("/book/update")
async def update(book: Book):
    BookRepo.update(book.id,book)
    return Response(code=200, status="Ok", message="Success update data").dict(exclude_none=True)


@router.delete("/book/{id}")
async def delete(id: str):
    BookRepo.delete(id)
    return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)
