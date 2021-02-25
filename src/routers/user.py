from typing import List, Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class CreateModel(BaseModel):
    user_name: str
    first_name: str
    last_name: str


class UpdateModel(BaseModel):
    id: int
    user_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]


@router.get("/user/", tags=["user"])
async def read_users(id: int):

    return [{"username": "t_yamada", "first_name": "Taro", "last_name": "Yamada"}]


@router.post("/user", tags=["user"])
async def create_user(body: List[CreateModel]):
    return JSONResponse(status_code=201, content={"message": "CREATED"})


@router.patch("/user", tags=["user"])
async def update_user(body: List[UpdateModel]):
    return JSONResponse(status_code=200, content={"message": "SUCCESS TO UPDATE"})