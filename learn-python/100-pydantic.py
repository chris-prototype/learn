from typing import TypedDict, Annotated
from pydantic import BaseModel, Field


# LangGraph uses annotions to pass reducer functions
def _last(a: str, b: str) -> str:
    return b if b else a


# this is a type dictionary used to define Factory State for langraph
class FactoryState(TypedDict):
    ticket_id: Annotated[str, _last]


# here is actual use of an annotation to not just check the type but also the value
class User(BaseModel):
    age: Annotated[int, Field(gt=0, le=120)]


User(age=0)   # raises ValidationError (gt = greater than)
User(age=1)   # valid
