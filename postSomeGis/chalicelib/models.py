from chalicelib.db import polyapi_connection
from geojson import Polygon
import json

def get_all_cities():
    res = polyapi_connection.execute("SELECT gid, ST_AsGeojson(gon) FROM cities;")
    # return all rows as a JSON array of objects
    return json.dumps([serialize_polygon(r) for r in res])


def validate_and_create_new_city(data):
    validation_result = _validate_new_city(data)
    if validation_result['result'] == 'failure':
        return validation_result
    return _create_new_city(data)

def _validate_new_city(data):
    required_fields = {'type', 'coordinates'}
    mising_fields = [ f for f in required_fields if f not in data.keys() ]
    if mising_fields:
        fields_string = ','.join(mising_fields)
        return {
            'result': 'failure',
            'error_code': 400,
            'error_message': 'The following fields are required: ' + fields_string
        }

    as_polygon = Polygon(data['coordinates'])
    if not as_polygon.is_valid:
        return {
            'result': 'failure',
            'error_code': 400,
            'error_message': as_polygon.errors()
        }

    return {'result': 'valid'}


def _create_new_city(data):
    result = polyapi_connection.execute(
        'INSERT INTO cities (gon) VALUES(ST_GeomFromGeoJSON(\'' + json.dumps(data) + '\'))'
        'RETURNING *;'
    )
    data['result'] = 'success' if result.rowcount > 0 else 'unknown failure'
    return data
    


def serialize_polygon(r):
    initial = dict(r)
    initial['st_asgeojson'] =  json.loads(initial['st_asgeojson'])
    return initial

