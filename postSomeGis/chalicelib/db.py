# chalicelib/db.py
from chalicelib import settings
from sqlalchemy import create_engine



DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=settings.DATABASE['USER'],
    pw=settings.DATABASE['PASSWORD'],
    url=settings.DATABASE['HOST'] + ':' + settings.DATABASE['PORT'],
    db=settings.DATABASE['NAME']
)
conn = create_engine(DB_URL).connect()