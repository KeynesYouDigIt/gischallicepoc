from chalice import Chalice
from chalicelib.models import get_all_cities

app = Chalice(app_name='postSomeGis')

@app.route('/polls/questions', methods=['GET', 'POST'])
def questions():
    request = app.current_request
    if request.method == 'POST':
        return 'YOU DID A POST :)'
    elif request.method == 'GET':
        print('yeyy')
        cities = get_all_cities()
        print(cities)
        # l = [
        #     {'id': city.id} 
        #     for city in cities
        # ]
        return cities