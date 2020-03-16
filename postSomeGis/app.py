from chalice import Chalice, Response
from chalicelib.models import get_all_cities, validate_and_create_new_city

app = Chalice(app_name='PolyApi')

@app.route('/cities', methods=['GET', 'POST'])
def questions():
    request = app.current_request
    if request.method == 'POST':
        result = validate_and_create_new_city(request.json_body)
        return Response(
            body=result,
            status_code=200 if result['result'] == 'success' else 400,
            headers={'Content-Type': 'application/json'}
        )

    elif request.method == 'GET':
        cities = get_all_cities()
        return Response(
            body=cities,
            status_code=200,
            headers={'Content-Type': 'application/json'}
        )
