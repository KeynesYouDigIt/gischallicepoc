from chalicelib import settings
from sqlalchemy import create_engine


def clean_setup():
    # Connect to the admin db and create the database for our app
    INITIAL_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/'.format(
        user=settings.DATABASE['USER'],
        pw=settings.DATABASE['PASSWORD'],
        url=settings.DATABASE['HOST'] + ':' + settings.DATABASE['PORT']
    )
    init_connection = create_engine(INITIAL_URL).connect()
    init_connection.connection.set_isolation_level(0)
    init_connection.execute('CREATE DATABASE ' + settings.DATABASE['NAME'])
    init_connection.connection.set_isolation_level(1)
    init_connection.close()

def set_schema(conn):
    conn.execute('CREATE EXTENSION postgis')
    conn.execute("""
        CREATE TABLE cities(gid serial PRIMARY KEY, gon geography(POLYGON));
    """)

def seed(conn):
    conn.execute("""
        INSERT INTO cities (gon) VALUES ('POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))');
        INSERT INTO cities (gon) VALUES ('POLYGON((-105.35 40.08, -105.1 40.08, -105.1 39.9, -105.35 39.9, -105.35 40.08))');
    """)

if __name__ == "__main__":
    print('Creating database!\n-\n')
    clean_setup()
    print('Database created, setting schema and seeding')

    # I hate to put an import this low, but it was the simpilest way
    # to make sure we dont try to connect you our database until its ready.

    # Given more time, I might set schema and seed in a seperate script.
    from chalicelib.db import polyapi_connection
    set_schema(polyapi_connection)
    seed(polyapi_connection)
