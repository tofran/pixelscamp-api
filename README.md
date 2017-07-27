# PixelsCamp-API [![pypi](https://img.shields.io/pypi/v/pixelscamp-api.svg)][pypi]
Pixels camp REST API wrapper in python.

You can find the official API documentation [here][API doc].

## To start..

Get it from [pypi] or this repo.

Import it: 

```from pixelscamp_api import PixelsAPI```

And initialize with:

```PixelsAPI(api_key="XXXXXXXXXXXXXXXX")```

or

```PixelsAPI(session="XXXXXXXX")```

or even: ```PixelsAPI()``` to use without authentication.

## Private user information (Authenticated)

```api.me()```

## List users (Non authenticated)

```api.users()```

or with some parameters: ```api.users(self, count=5, offset=0)```

## User public data (Non authenticated)

```api.user('username')```

## List badges (Non authenticated )

```api.badges_list()```

## List badges owners (Non authenticated)

```api.badges_owners(92)```

## Redeem a badge (Authenticated)

```api.badges_redeem('XXXXXXX', 'username')```

or with: ```api.badges_redeem('XXXXXXX')```, it will automatically retrive your username with  ```me()```.


[API doc]: https://github.com/PixelsCamp/docs/blob/master/API.md
[pypi]: https://pypi.python.org/pypi/pixelscamp-api
