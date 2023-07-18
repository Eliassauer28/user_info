from unittest.mock import MagicMock
from flask import jsonify
import pytest
from src.allocation.views import get_users_info


@pytest.fixture
def mock_uow():
    return MockUnitOfWork()

@pytest.fixture
def mock_make_response():
    return MagicMock()

@pytest.fixture
def mock_jsonify():
    return MagicMock()

class MockUnitOfWork:
    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def get_users_info(uow):
    with uow:
        results = uow.users.get_user_info()
    return results

def get_users_info_endpoint(uow):
    users_info = get_users_info(uow)
    return jsonify(users_info)

def test_get_users_info(mock_uow):
    mock_users_repo = MagicMock()
    mock_uow.users = mock_users_repo

    mock_result = [
        {"name": "John Doe", "email": "john.doe@example.com", "role_description": "developer", "claim_description": "Admin"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "role_description": "manager", "claim_description": "User"},
    ]
    mock_users_repo.get_user_info.return_value = mock_result

    result = get_users_info(mock_uow)

    assert result == mock_result
