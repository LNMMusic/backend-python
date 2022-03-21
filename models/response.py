from pydantic   import BaseModel
from typing     import Optional


class Response(BaseModel):
    message:    Optional[str]
    data:       Optional[str]