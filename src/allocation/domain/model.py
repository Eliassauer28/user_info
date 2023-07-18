from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    role_id: int
    created_at: date
    updated_at: Optional[date]


@dataclass
class Role:
    role_id: int
    description: str


@dataclass
class Claim:
    id: int
    description: str
    active: bool


@dataclass
class UserClaim:
    user_id: int
    claim_id: int
