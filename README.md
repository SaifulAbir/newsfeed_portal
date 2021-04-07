# Newsfeed Portal
## How to run the project:

After creating and activating the virtual environment run the following command to install all the packages.

`pip install -r requirements.txt`

Next to migrate run:

`python manage.py migrate`

Then run the project with the following command:

`python manage.py runserver`

API endpoint for creating new user account:

``POST /auth/users/``

Example request and JSON input format:

http://127.0.0.1:8000/auth/users/

```
{
    "email": "saiful@example.com",
    "username": "abir",
    "password": "pass876512"
}
```

Example Response:

```
{
    "email": "saiful@example.com",
    "username": "abir",
    "id": 2
}
```
Create a JWT by passing a valid user in the post request to this endpoint:

``POST /auth/jwt/create/``

Example request and JSON input format:

http://127.0.0.1:8000/auth/jwt/create

```
{
    "username": "abir",
    "password": "pass876512"
}
```
Example Response:

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNzg4ODc0MCwianRpIjoiNmM1NWFmM2UzZDkyNDI0YjhkYmI5YWZjY2NhOGRlMzgiLCJ1c2VyX2lkIjoxfQ.LeVIkhALBIYn3l8bbxF-aeZNfXxsiznOiXJFIGCG2nQ",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3ODAyNjQwLCJqdGkiOiI4YjY4NDNmODhhNTM0MmVlODJlNzI4NWVlNTM3MzVlNyIsInVzZXJfaWQiOjF9.K13yK9aKVHZjqpDbk9gz__njqEmR6bbwFrYFMSRkkOU"
}
```
Get a new JWT once the lifetime of the previously generated one expires:

``POST /auth/jwt/refresh/``

Example request and JSON input format:

http://127.0.0.1:8000/auth/jwt/refresh

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNzkwNzM0NywianRpIjoiOGM4ZTE3Yzg4MTJhNDc0NTg0ZjE2YzRiNzA0YTgwOTYiLCJ1c2VyX2lkIjoxfQ.WNU2cnB5N5IGUIrNudmuQHfi1VqLLTiYHxjRB3Vmzew"
}
```
Example Response:

```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3ODIxMjcyLCJqdGkiOiIyNDNmZTJiYzUxNDk0MjIyODc1OTdmNGFlYjhhYzYyMyIsInVzZXJfaWQiOjF9.YYfAiKo9sqT3Q1eXAIWDa_LaXKyyxZ6AeBU9qYzoTWM"
}
```
