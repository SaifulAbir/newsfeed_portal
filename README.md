# Newsfeed Portal
## How to run the project:

After creating and activating the virtual environment run the following command to install all the packages.

`pip install -r requirements.txt`

Next to migrate run:

`python manage.py migrate`

Then run the project with the following command:

`python manage.py runserver`

#### API endpoint for creating new user account:

``POST /auth/users/``

Example request and JSON input format:

http://127.0.0.1:8000/auth/users/

```json
{
    "email": "saiful@example.com",
    "username": "abir",
    "password": "pass876512"
}
```

Example Response:

```json
{
    "email": "saiful@example.com",
    "username": "abir",
    "id": 2
}
```
#### Create a JWT by passing a valid user in the post request to this endpoint:

``POST /auth/jwt/create/``

Example request and JSON input format:

http://127.0.0.1:8000/auth/jwt/create

```json
{
    "username": "abir",
    "password": "pass876512"
}
```
Example Response:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNzg4ODc0MCwianRpIjoiNmM1NWFmM2UzZDkyNDI0YjhkYmI5YWZjY2NhOGRlMzgiLCJ1c2VyX2lkIjoxfQ.LeVIkhALBIYn3l8bbxF-aeZNfXxsiznOiXJFIGCG2nQ",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3ODAyNjQwLCJqdGkiOiI4YjY4NDNmODhhNTM0MmVlODJlNzI4NWVlNTM3MzVlNyIsInVzZXJfaWQiOjF9.K13yK9aKVHZjqpDbk9gz__njqEmR6bbwFrYFMSRkkOU"
}
```
#### Get a new JWT once the lifetime of the previously generated one expires:

``POST /auth/jwt/refresh/``

Example request and JSON input format:

http://127.0.0.1:8000/auth/jwt/refresh

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNzkwNzM0NywianRpIjoiOGM4ZTE3Yzg4MTJhNDc0NTg0ZjE2YzRiNzA0YTgwOTYiLCJ1c2VyX2lkIjoxfQ.WNU2cnB5N5IGUIrNudmuQHfi1VqLLTiYHxjRB3Vmzew"
}
```
Example Response:

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3ODIxMjcyLCJqdGkiOiIyNDNmZTJiYzUxNDk0MjIyODc1OTdmNGFlYjhhYzYyMyIsInVzZXJfaWQiOjF9.YYfAiKo9sqT3Q1eXAIWDa_LaXKyyxZ6AeBU9qYzoTWM"
}
```
#### API endpoint to set the value of settings:

``POST /api/settings/create/``

| :heavy_check_mark:  Make sure you pass the bearer token in the authorization header before giving request|
|----------------------------------------------------------------------------------------------------------|

Example request and JSON input format:

http://127.0.0.1:8000/api/settings/create/

```json
{
    "countries": "ae, us, cn",
    "sources": "cnn, google-news",
    "keywords": "covid, pandemic, daily"
}
```
Example Response:

```json
{
    "id": 9,
    "countries": [
        {
            "id": 1,
            "name": "ae"
        },
        {
            "id": 2,
            "name": "us"
        },
        {
            "id": 4,
            "name": "cn"
        }
    ],
    "sources": [
        {
            "id": 3,
            "name": "cnn"
        },
        {
            "id": 4,
            "name": "google-news"
        }
    ],
    "keywords": [
        {
            "id": 1,
            "name": "covid"
        },
        {
            "id": 6,
            "name": "pandemic"
        },
        {
            "id": 7,
            "name": "daily"
        }
    ],
    "user": {
        "id": 2,
        "username": "abir",
        "email": "saiful@example.com",
        "is_active": true
    },
    "created_by": "2",
    "created_at": "2021-04-08T10:43:22.015080Z",
    "created_from": "127.0.0.1",
    "modified_by": null,
    "modified_at": null,
    "modified_from": null
}
```
#### API endpoint to update the value of settings:

``POST /api/settings/update/``

| :heavy_check_mark:  Make sure you pass the bearer token in the authorization header before giving request|
|----------------------------------------------------------------------------------------------------------|

Example request and JSON input format:

http://127.0.0.1:8000/api/settings/update/

```json
{
    "countries": "us",
    "sources": "cnn, google-news",
    "keywords": "covid, pandemic, accident"
}
```
Example Response:

```json
{
    "id": 9,
    "countries": [
        {
            "id": 2,
            "name": "us"
        }
    ],
    "sources": [
        {
            "id": 3,
            "name": "cnn"
        },
        {
            "id": 4,
            "name": "google-news"
        }
    ],
    "keywords": [
        {
            "id": 1,
            "name": "covid"
        },
        {
            "id": 6,
            "name": "pandemic"
        },
        {
            "id": 8,
            "name": "accident"
        }
    ],
    "user": {
        "id": 2,
        "username": "abir",
        "email": "saiful@example.com",
        "is_active": true
    },
    "created_by": "2",
    "created_at": "2021-04-08T10:43:22.015080Z",
    "created_from": "127.0.0.1",
    "modified_by": "2",
    "modified_at": "2021-04-08T10:46:58.329824Z",
    "modified_from": "127.0.0.1"
}
```
#### API endpoint of user settings details:

``GET /api/settings/details/``

| :heavy_check_mark:  Make sure you pass the bearer token in the authorization header before giving request|
|----------------------------------------------------------------------------------------------------------|

Example request:

http://127.0.0.1:8000/api/settings/details/

Example Response:

```json
{
    "id": 9,
    "countries": [
        {
            "id": 2,
            "name": "us"
        }
    ],
    "sources": [
        {
            "id": 3,
            "name": "cnn"
        },
        {
            "id": 4,
            "name": "google-news"
        }
    ],
    "keywords": [
        {
            "id": 1,
            "name": "covid"
        },
        {
            "id": 6,
            "name": "pandemic"
        },
        {
            "id": 8,
            "name": "accident"
        }
    ],
    "user": {
        "id": 2,
        "username": "abir",
        "email": "saiful@example.com",
        "is_active": true
    },
    "created_by": "2",
    "created_at": "2021-04-08T10:43:22.015080Z",
    "created_from": "127.0.0.1",
    "modified_by": "2",
    "modified_at": "2021-04-08T10:46:58.329824Z",
    "modified_from": "127.0.0.1"
}
```

## I have used django celery beat to fetch the top headlines periodically every 10 minutes

| :heavy_exclamation_mark:  As a message broker I used RabbitMQ|
|----------------------------------------------------------------------------------------------------------|

**Installing RabbitMQ on Ubuntu**

``apt-get install rabbitmq-server``

**Installing RabbitMQ on Mac**

``brew install rabbitmq``

**For other operating systems, check the [Downloading and Installing RabbitMQ on their Website.](https://www.rabbitmq.com/download.html)**

#### Now run Celery with the command:

``celery -A newsfeed_portal worker -l info``

#### To start the celery beat service run command:

``celery -A newsfeed_portal beat -l info``

Now it should fetch top headlines every 10 minutes

#### API endpoint of personalized news feed:

``GET /api/news-feed/``

| :heavy_check_mark:  Make sure you pass the bearer token in the authorization header before giving request|
|----------------------------------------------------------------------------------------------------------|

Example request:

http://127.0.0.1:8000/api/news-feed/

Example Response:

```
