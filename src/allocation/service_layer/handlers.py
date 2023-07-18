# pylint: disable=unused-argument
from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING
import logging
from src.allocation.domain import commands, model
from src.allocation.service_layer.enums import RoleEnum

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from . import unit_of_work

def add_user(cmd: commands.CreateUser, uow: unit_of_work.AbstractUnitOfWork):
    try:
        with uow:
            role = uow.users.get_role_by_id(cmd.role_id.value)
            if not role:
                role = model.Role(role_id=cmd.role_id.value, description=RoleEnum(cmd.role_id).name)
                uow.users.add_user_role(role)
                uow.commit()

            user = model.User(
                id=None,
                name=cmd.name,
                email=cmd.email,
                password=cmd.password,
                role_id=cmd.role_id.value,
                created_at=cmd.created_at,
                updated_at=None
            )

            description = "Admin" if cmd.role_id.value == RoleEnum.DEVELOPER.value else "User"
            claim = model.Claim(id=None, description=description, active=True)
            user_claim = model.UserClaim(user_id=user.id, claim_id=claim.id)

            uow.users.add_user_info(
                user=user, claim=claim, user_claim=user_claim)

            uow.commit()

    except Exception as e:
        logger.error("Failed to add user to the database: %s", str(e))
        raise  





EVENT_HANDLERS = {

}

COMMAND_HANDLERS = {
    commands.CreateUser: add_user
}  # type: Dict[Type[commands.Command], Callable]
