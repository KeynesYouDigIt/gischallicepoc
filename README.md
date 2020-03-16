
# PolyAPI

This chalice API supports the creation and storage of Polygons using postgis.

## Setup
1. Install Dependencies
    All requirements are listed in the Pipfile. Create a new virtual environment with these dependencies by running `$ pipenv install`.

2. Environment Setup
    
    Next, create a `.env` file. This will automatically set environmental variables for anything run under `pipenv run`. In this app, these are used to securely connect to the database.

    The file should look like this
    ```
    export DB_HOST={Host machine for the db, localhost should work for a dev setup}
    export DB_PORT={Port exposed}
    export DB_NAME={What you would like the database to be named}
    export DB_USER={An existing user in postgres with privileges to create a new database}
    export DB_PASSWORD={The same user's password}
    ```

    Note that this file is git ignored.

3. Install/Connect Database
    The next step is to run a database supporting the PostGIS extention. I found MDillion's docker image did the trick - it can be pulled by running 
    `$ docker pull mdillon/postgis`.

    Run the container mapping the port you would like to expose properly. 
    `$ docker run -d -p 5432:5432  mdillon/postgres`

    You can also run Postgres outside of a container if you prefer. [Consult the PostGIS setup documentation to do this](https://postgis.net/install/).

4. Database setup and seed script
    To check that your Postgres container is running and to setup, schematize, and seed your database, run the `database_setup.py` script within the pipenv environment. 
    `$ pipenv run python database_setup.py`

5. You should now be able to run `$ pipenv run chalice local` and see the app start serving locally.

## Endpoint Documentation
For now, there is only a single endpoint to create and list polygons (representing cities... theoretically).

`/cities` accepts GET and POST requests.


A GET will list all city polygons stored in GeoJSON format
(sample response)
```
[
    {
        "gid": 1,
        "st_asgeojson": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        0,
                        0
                    ],
                    [
                        1,
                        0
                    ],
                    [
                        1,
                        1
                    ],
                    [
                        0,
                        1
                    ],
                    [
                        0,
                        0
                    ]
                ]
            ]
        }
    },
    {
        "gid": 2,
        "st_asgeojson": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -105.35,
                        40.08
                    ],
                    [
                        -105.1,
                        40.08
                    ],
                    [
                        -105.1,
                        39.9
                    ],
                    [
                        -105.35,
                        39.9
                    ],
                    [
                        -105.35,
                        40.08
                    ]
                ]
            ]
        }
    },
```

And a post will add a polygon (also GeoJSON format)
(sample request)
```
{
    "type": "Polygon",
    "coordinates": [
        [
            [
                -105.35,
                40.08
            ],
            [
                -105.1,
                40.08
            ],
            [
                -105.1,
                39.9
            ],
            [
                -105.35,
                39.9
            ],
            [
                -105.35,
                40.08
            ]
        ]
    ]
}
```
(sample response)
```
{
    "type": "Polygon",
    "coordinates": [
        [
            [
                -105.35,
                40.08
            ],
            [
                -105.1,
                40.08
            ],
            [
                -105.1,
                39.9
            ],
            [
                -105.35,
                39.9
            ],
            [
                -105.35,
                40.08
            ]
        ]
    ],
    "result": "success"
}
```