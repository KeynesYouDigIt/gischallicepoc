# chalicelib/models.py
from sqlalchemy import Column
from chalicelib.db import conn
from geoalchemy2 import Geometry
import json

def get_all_cities():
    res = conn.execute("SELECT gid, ST_AsGeojson(gon) FROM cities;")

    # return all rows as a JSON array of objects
    return json.dumps([serialize_polygon(r) for r in res])

    # return conn.execute("SELECT * FROM city;")

def serialize_polygon(r):
    initial = dict(r)
    initial['st_asgeojson'] =  json.loads(initial['st_asgeojson'])
    return initial

def setup_and_seed():
    conn.execute("""
        CREATE TABLE cities(gid serial PRIMARY KEY, gon geography(POLYGON));
    """)

    conn.execute("""
        INSERT INTO cities (gon) VALUES ('POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))');
        INSERT INTO cities (gon) VALUES ('POLYGON((-105.35 40.08, -105.1 40.08, -105.1 39.9, -105.35 39.9, -105.35 40.08))');
    """)

#setup_and_seed()