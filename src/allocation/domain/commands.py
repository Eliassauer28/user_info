# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from datetime import date
from typing import Optional

from src.allocation.service_layer.enums import RoleEnum


class Command:
    pass


@dataclass
class CreateUser(Command):
    name: str
    email: str
    password: str
    role_id: RoleEnum
    created_at: date
    updated_at: Optional[date]


