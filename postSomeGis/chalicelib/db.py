from chalicelib import settings
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def _get_connection():
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=settings.DATABASE['USER'],
        pw=settings.DATABASE['PASSWORD'],
        url=settings.DATABASE['HOST'] + ':' + settings.DATABASE['PORT'],
        db=settings.DATABASE['NAME']
    )
    try:
        return create_engine(DB_URL).connect()
    except OperationalError as e:
        raise Exception(
            'Could not connect to database! \n'
            'If the container is running and can be connected to, please ensure the setup script has been run.\n'
            'Message from database is - ' + e.args[0]
        )

polyapi_connection = _get_connection()