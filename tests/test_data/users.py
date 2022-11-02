from dataclasses import dataclass


@dataclass
class User:
    first_name: str = 'Ivan'
    last_name: str = 'Ivanov'
    email: str = 'ivanov@test.test'
    job: str = 'IT specialist'
    id: str = '2'
    password: str = 'password'
    token: str = 'token'


my_user = User()
system_user = User(
    first_name='Janet',
    last_name='Weaver',
    email='eve.holt@reqres.in',
    password='cityslicka',
    token='QpwL5tke4Pnpja7X4'
)
