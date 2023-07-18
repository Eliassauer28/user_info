import logging
from sqlalchemy import (
    Boolean,
    PrimaryKeyConstraint,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import mapper, relationship
from src.allocation.domain import model

logger = logging.getLogger(__name__)

metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('role_id', Integer, primary_key=True),
    Column('description', String, nullable=False)
)

claims = Table(
    'claims',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('active', Boolean, nullable=False, default=True)
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False),
    Column('role_id', Integer, ForeignKey('roles.role_id'), nullable=False),
    Column('created_at', Date, nullable=False),
    Column('updated_at', Date)
)

user_claims = Table(
    'user_claims',
    metadata,
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('claim_id', Integer, ForeignKey('claims.id'), nullable=False),
    PrimaryKeyConstraint('user_id', 'claim_id')
)


def start_mappers():
    logger.info("Starting mappers")
    roles_mapper = mapper(model.Role, roles)
    mapper(model.Claim, claims)
    mapper(
        model.User,
        users,
        properties={"role": relationship(roles_mapper)}
    )
    mapper(
        model.UserClaim,
        user_claims,
        properties={
            "user": relationship(model.User, backref="user_claims"),
            "claim": relationship(model.Claim, backref="user_claims")
        }
    )
