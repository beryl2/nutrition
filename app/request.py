from app import app
from urllib import request,json
import urllib.request,json
from .models import egg
def post_():
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

    userquery = {
     "query":"egg"
    }
    req = request.Request(url, method ='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('x-app-id','db6249ef')
    req.add_header('x-app-key','5f05ca24b7db75fd0d05102571367378')
    data = json.dumps(userquery)
    data = data.encode()

    with request.urlopen(req, data = data.encode()) as url:
        unsorteddata = url.read()
    return unsorteddata

def unsorted(userquery_list):
    components = []
    for unsorted_item in userquery_list:
        id = unsorted_item.post('id')
        food_name = unsorted_item.post('food_name')
        serving_qty = unsorted_item.post('serving_qty')
        serving_unit = unsorted_item.post('serving_unit')
        images = unsorted_item.post('images')

        userquery = egg(id, food_name,serving_qty, serving_unit, images)
        components.append(userquery)

    return components


    #search process
def search():
    search_url =  'https://trackapi.nutritionix.com/v2/natural/nutrients'.format('userquery')
    userquery = {
     "query":"egg"
    }
    req = request.Request(search_url, method ='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('x-app-id','db6249ef')
    req.add_header('x-app-key','5f05ca24b7db75fd0d05102571367378')
    data = json.loads(userquery)
    data = data.encode()

    with request.urlopen(req, data = data.encode()) as url:
        output = url.read()
        main =json.loads(output)
    return main 

def userquery(userquery_list):
    output = []
    for userquery_item in userquery_list:
        id = userquery_item.post('id')
        food_name = userquery_item.post('food_name')
        serving_qty = userquery_item.post('serving_qty')
        serving_unit = userquery_item.post('serving_unit')
        images = userquery_item.post('images')
        userquery = egg(id, food_name,serving_qty, serving_unit, images)
        


        if images:
            imageoutput = egg(id,food_name,serving_qty,serving_unit, images)
            imageoutput.append(userquery)

    return imageoutput

