from fastapi import APIRouter, status, Body, Path

from cryptography.fernet import Fernet

from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)

@user.get(
    path='/users',
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users'])
def get_all_users():
    """
    Show all users 

    Returns:
        All the users
    """
    return conn.execute(users.select()).fetchall()


@user.post(
    path='/users',
    status_code=status.HTTP_201_CREATED,
    summary='Create a user',
    tags=['Users']
    )
def create_user(user: User = Body(
    example={
    "name": "Samuel Smith",
    "email": "samu.s12@gmail.com",
    "password": "whiteelephant123"},
    )):
    """
    Create a user.

    Return: 
        The user that was be created
    """
    new_user = {'name':user.name, 'email':user.email}
    # Encrypting the password
    new_user['password'] = f.encrypt(user.password.encode('utf-8'))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get(
    path='/users/{id}',
    summary='Update a user',
    status_code=status.HTTP_200_OK,
    tags=['Users'])
def get_user (id: str = Path(
    title='User id',
    description='The id of the user that you want see.',
    example=10
)):
    response = conn.execute(users.select().where(users.c.id == id)).first()
    return response


@user.delete(
    path='/users/{id}',
    summary='Delete a user',
    tags=['Users'],
    status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str = Path(
    title='User id',
    description='The id of the user that you want eliminate.',
    example='7'
)):
    conn.execute(users.delete().where(users.c.id == id))
    return 


@user.put(
    path='/users/{id}',
    summary='Update a user',
    status_code=status.HTTP_200_OK,
    tags=['Users'])
def update_user(id: str, user: User):
    # add the logic so that it doesn't change values ​
    # ​that the user doesn't want to change
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=f.encrypt(user.password.encode('utf-8'))
    ).where(users.c.id == id)) 
    return 'User was updated'