from datetime import datetime
from typing import Optional
from pydantic.fields import Field
from pydantic import BaseModel
import secrets
from src.allocation.domain.commands import CreateUser
from src.allocation.service_layer.enums import RoleEnum



class UserDTO(BaseModel):
    name: str = Field(..., title="user name")
    email: str = Field(..., title="user email")
    role_id: RoleEnum  = Field(..., title="user role")
    password: Optional[str] = Field(secrets.token_urlsafe(), title="user password")

    def getCommand(self):
        return CreateUser(
            name = self.name,
            email= self.email,
            role_id=self.role_id,
            password=self.password,
            created_at=datetime.now(),
            updated_at=None
        )




