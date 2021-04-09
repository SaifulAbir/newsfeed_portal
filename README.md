# Newsfeed Portal
## How to run the project:

### Assuming you have Python3 installed on your machine

##### Install Pip on Ubuntu:

``sudo apt install python3 python3-pip -y``

##### Install Pip on MacOS:

``sudo easy_install pip``

**For other operating systems, check the [Installation on pip documentation.](https://pip.pypa.io/en/stable/installing/)**

##### Install virtualenv and create venv and activate on Ubuntu and MacOS:
```pip install virtualenv```\
```virtualenv -p python3 venv```\
```source venv/bin/activate```

After creating and activating the virtual environment run the following command to install all the packages.

`pip install -r requirements.txt`

| :heavy_check_mark:  By default sqlite3 will be used as a database but you can switch to mysql. For that you have to uncomment mysql configuration.|
|--------------------------------------------------------------------------------------------------------------------------------------------------|

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
    "countries": "us, de",
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
        },
        {
            "id": 5,
            "name": "de"
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
        },
        {
            "id": 5,
            "name": "spiegel-online"
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
    "modified_at": "2021-04-08T17:29:00.245862Z",
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
        },
        {
            "id": 5,
            "name": "de"
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
        },
        {
            "id": 5,
            "name": "spiegel-online"
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
    "modified_at": "2021-04-08T17:29:00.245862Z",
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
[
    {
        "headline": "Paint plant explosion leaves one person unaccounted for and several injured - CNN ",
        "thumbnail": "https://cdn.cnn.com/cnnnext/dam/assets/210408090605-01-ohio-paint-facility-explosion-screengrab-super-tease.jpg",
        "news_url": "https://www.cnn.com/2021/04/08/us/ohio-paint-facility-explosion/index.html",
        "source_of_news": "cnn",
        "country_of_news": "us",
        "published_at": "2021-04-08T13:10:00Z"
    },
    {
        "headline": "Khloé Kardashian shows unedited body to address unauthorized photo release - CNN ",
        "thumbnail": "https://cdn.cnn.com/cnnnext/dam/assets/210408115442-khloe-kardashian-ig-grab-super-tease.jpg",
        "news_url": "https://www.cnn.com/2021/04/08/entertainment/khloe-kardashian-unedited-photo/index.html",
        "source_of_news": "cnn",
        "country_of_news": "us",
        "published_at": "2021-04-08T11:41:00Z"
    },
    {
        "headline": "Fauci: Almost a race between vaccinations and the surge - CNN ",
        "thumbnail": "https://cdn.cnn.com/cnnnext/dam/assets/210408083623-dr-anthony-facui-for-video-april-7-2021-super-tease.jpg",
        "news_url": "https://www.cnn.com/videos/health/2021/04/08/anthony-fauci-race-between-vaccine-and-surge-sot-ac360-vpx.cnn",
        "source_of_news": "cnn",
        "country_of_news": "us",
        "published_at": "2021-04-08T12:39:45Z"
    },
    {
        "headline": "Bill Owens obituary: Dolly Parton's uncle dies at 85 - Legacy.com",
        "thumbnail": null,
        "news_url": "https://news.google.com/__i/rss/rd/articles/CBMidGh0dHBzOi8vd3d3LmxlZ2FjeS5jb20vbmV3cy9jZWxlYnJpdHktZGVhdGhzL2JpbGwtb3dlbnMtMTkzNS0yMDIxLXNvbmd3cml0ZXItd2hvLXdhcy1kb2xseS1wYXJ0b25zLXVuY2xlLWFuZC1tZW50b3Iv0gEA?oc=5",
        "source_of_news": "google-news",
        "country_of_news": "us",
        "published_at": "2021-04-08T14:00:36Z"
    },
    {
        "headline": "Sophie Turner REACTS to Taylor Swift's Song Seemingly About Joe Jonas - Entertainment Tonight",
        "thumbnail": null,
        "news_url": "https://news.google.com/__i/rss/rd/articles/CBMiK2h0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9djRNQm95VV8xejDSAQA?oc=5",
        "source_of_news": "google-news",
        "country_of_news": "us",
        "published_at": "2021-04-08T13:00:31Z"
    },
    {
        "headline": "Techinvestor: Peter Thiel nennt Bitcoin »eine chinesische Finanzwaffe« - DER SPIEGEL",
        "thumbnail": "https://cdn.prod.www.spiegel.de/images/196a0934-c7b4-489f-b199-712b8343339a_w1280_r1.77_fpx49_fpy29.jpg",
        "news_url": "https://www.spiegel.de/wirtschaft/bitcoin-peter-thiel-warnt-vor-chinesischer-finanzwaffe-a-7c5a4f3a-64d6-4822-8cb3-0e635522ddc4",
        "source_of_news": "spiegel-online",
        "country_of_news": "de",
        "published_at": "2021-04-08T13:36:17Z"
    },
    {
        "headline": "Mehr Bundeskompetenz in der Pandemie: 52 Unionsabgeordnete unterstützen Änderung des Infektionsschutzgesetzes - DER SPIEGEL",
        "thumbnail": "https://cdn.prod.www.spiegel.de/images/7b1320a9-4f16-4206-854c-432b601eb2cf_w1280_r1.77_fpx47_fpy49.jpg",
        "news_url": "https://www.spiegel.de/politik/deutschland/infektionsschutzgesetz-52-unionsabgeordnete-unterstuetzen-initiative-fuer-machtausbau-a-46ad1eac-f946-460a-acda-2b4f5e7e8eff",
        "source_of_news": "spiegel-online",
        "country_of_news": "de",
        "published_at": "2021-04-08T13:26:49Z"
    }
]
```
##### User also will get an email notification if keyword appears on their personalized newsfeed.

##### Reset password api endpoint:

``POST /auth/users/set_password/``

| :heavy_check_mark:  Make sure you pass the bearer token in the authorization header before giving request|
|----------------------------------------------------------------------------------------------------------|

Example request and JSON input format:

http://127.0.0.1:8000/auth/users/set_password/

```json
{
    "new_password": "87654321a",
    "current_password": "pass876512"
}
```
**Run all tests with command:**

``python manage.py test --verbosity 2``
