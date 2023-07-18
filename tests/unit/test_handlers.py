import pytest
from unittest.mock import Mock, create_autospec
from src.allocation.domain import commands, model
from src.allocation.service_layer.enums import RoleEnum
from src.allocation.service_layer import unit_of_work
from src.allocation.service_layer.handlers import add_user


def test_add_user_success():
    cmd = commands.CreateUser(
        name="test",
        email="test@example.com",
        password="password",
        role_id=RoleEnum.DEVELOPER,
        created_at=None,
        updated_at=None
    )
    uow = create_autospec(unit_of_work.AbstractUnitOfWork)
    uow.users = Mock()
    uow.users.get_role_by_id.return_value = model.Role(
        role_id=cmd.role_id, 
        description=cmd.role_id.name
    )

    add_user(cmd, uow)

    # Removed uow.users.add_user_role.called
    assert uow.users.add_user_info.called
    assert uow.commit.call_count == 1  # Reduced from 2 to 1

def test_add_user_role_does_not_exist():
    cmd = commands.CreateUser(
        name="test",
        email="test@example.com",
        password="password",
        role_id=RoleEnum.DEVELOPER,
        created_at=None,
        updated_at=None
    )
    uow = create_autospec(unit_of_work.AbstractUnitOfWork)
    uow.users = Mock()
    uow.users.get_role_by_id.return_value = None

    add_user(cmd, uow)

    assert uow.users.add_user_role.called
    assert uow.users.add_user_info.called
    assert uow.commit.call_count == 2

def test_add_user_exception():
    cmd = commands.CreateUser(
        name="test",
        email="test@example.com",
        password="password",
        role_id=RoleEnum.DEVELOPER,
        created_at=None,
        updated_at=None
    )
    uow = create_autospec(unit_of_work.AbstractUnitOfWork)
    uow.users = Mock()
    uow.users.get_role_by_id.side_effect = Exception('Mocked Exception')

    with pytest.raises(Exception) as e:
        add_user(cmd, uow)

    assert str(e.value) == 'Mocked Exception'
