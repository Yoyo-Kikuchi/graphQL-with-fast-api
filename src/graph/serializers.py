from typing import List, Optional
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class UserModel(BaseModel):
    id: Optional[int]
    user_name: str
    first_name: str
    last_name: str

class UserInfoModel(PydanticObjectType):
    class Meta:
        model = UserModel


class UserCreateModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('id', )