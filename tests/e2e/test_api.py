
import random
import requests
from src.allocation import config
import pytest

url = config.get_api_url()

@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_add_user():
    r = requests.post(
        f'{url}/add_user',
        json={
            "name": "Gato",
            "email": "gato@gmail.com",
            "role_id": 1
        }
    )
    assert r.status_code == 200


@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_get_users_info():

    r = requests.get(f'{url}/users')
    assert r.status_code == 200

@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_get_role():
    r = requests.get(f'{url}/role?role_id={1}')
    assert r.status_code == 200
    assert r.json() ==  {
    "description": "DEVELOPER",
    "role_id": 1
}

@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_get_role_missing_role_id():
    r = requests.get(f'{url}/role')
    assert r.status_code == 404
    assert r.json() == {"error": "role_id must not be null"}   

@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_get_role_not_found():
    r = requests.get(f'{url}/role?role_id=500')
    assert r.status_code == 404
    assert r.json() == {"error": "Not found"}  
