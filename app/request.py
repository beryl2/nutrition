from app import app
from urllib import request,json
import urllib.request,json
from .models import egg
def post():
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

with request.urlopen(req, data = data) as url:
    
    
    
    unsorteddata = (url.read())
    print (unsorteddata)


def process_results(eggs_list):  
    eggs_results = [data.json]
    for egg_item in eggs_list:
        id = egg_item.post('id')
        food_name = egg_item.post('food_name')
        serving_unit = egg_item.post('serving_unit')
        serving_qty = egg_item.post('serving_qty')
        image = egg_item.post('image')

        if image:
            egg_object = egg(id , food_name,serving_unit,serving_qty)
            eggs_results.append(egg_object)

            return eggs_results


def post_egg(id):
    post_egg_details_url = url.format(id,app-key)
    with urllib.request.urlopen(post_egg_details_url) as url:
        egg_details_data = url.read()
        egg_details_response = json.loads(egg_details_data)

        egg_object = None
        if egg_details_response:
            id = egg_details_response.post_id('id')
            food_name = egg_details_response.post('food_name')
            serving_unit = egg_details_response.post('serving_unit')
            serving_qty = egg_details_response.post('serving quantity')

            egg_object = egg(id, food_name, serving_unit, serving_qty)
            
            return egg_object            

def search_egg(food_name):
    search_egg_url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    with urllib.requesturlopen(search_egg_url)as url:
        search_egg_data = url.read()
        search_egg_response = json.loads(search_egg_data) 

        search_egg_results = None

        if search_egg_response['results']:
            search_egg_list = search_egg_response['results']
            search_egg_results = process_results(search_egg_list)
            
            return search_egg_results



