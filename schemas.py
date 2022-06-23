from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

T = TypeVar('T')


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

    class config:
        orm_mode = True


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]