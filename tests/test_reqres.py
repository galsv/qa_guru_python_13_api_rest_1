from requests import Response
from pytest_voluptuous import S
from schemas import user_schema
from tests.test_data.users import my_user, system_user

from utils.base_session import reqres_session


def test_create_user():
    name = f'{my_user.first_name} {my_user.last_name}'

    result: Response = reqres_session().post(
        url='/api/users',
        json={'name': name, 'job': my_user.job}
    )

    my_user.id = result.json()['id']

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == my_user.job
    assert result.json() == S(user_schema.create_user)


def test_get_user():
    result: Response = reqres_session().get(
        url=f'/api/users/{system_user.id}',
    )

    assert result.status_code == 200
    assert result.json()['data']['id'] == int(system_user.id)
    assert result.json()['data']['first_name'] == system_user.first_name
    assert result.json()['data']['last_name'] == system_user.last_name
    assert result.json() == S(user_schema.get_user)


def test_update_user():
    my_user.first_name = "Petrov"
    my_user.last_name = "Petr"
    my_user.job = "Project Manager"
    name = f'{my_user.first_name} {my_user.last_name}'

    result: Response = reqres_session().put(
        url=f'/api/users/{system_user.id}',
        json={'name': name, 'job': my_user.job}
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == my_user.job
    assert result.json() == S(user_schema.update_user)


def test_user_login():
    result: Response = reqres_session().post(
        url='/api/login',
        json={'email': system_user.email, 'password': system_user.password}
    )

    assert result.status_code == 200
    assert result.json()['token'] == system_user.token
    assert result.json() == S(user_schema.user_login)


def test_delete_user():
    result: Response = reqres_session().delete(
        url=f'/api/users/{my_user.id}',
    )

    assert result.status_code == 204
