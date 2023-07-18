from src.allocation.service_layer import unit_of_work
from unittest.mock import MagicMock
from src.allocation.domain import commands

from src.allocation.service_layer.handlers import add_user

def test_add_user():
    mock_users_repo = MagicMock()
    mock_uow = MagicMock(spec=unit_of_work.AbstractUnitOfWork)
    mock_cmd = MagicMock(spec=commands.CreateUser)

    mock_uow.users = mock_users_repo
    mock_users_repo.add_user_info.return_value = None

    mock_cmd.name = "John Doe"
    mock_cmd.email = "john.doe@example.com"
    mock_cmd.password = "password123"
    mock_cmd.role_id = 1
    mock_cmd.created_at = "2023-07-09"

    add_user(mock_cmd, mock_uow)

    assert mock_uow.__enter__.called
    assert mock_users_repo.add_user_info.called
    assert mock_uow.commit.called
    assert mock_uow.__exit__.called
