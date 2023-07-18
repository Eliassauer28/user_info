from pydantic.fields import Field
from pydantic import BaseModel


class UserDTO(BaseModel):
    role_id: str = Field(...)

    
    



