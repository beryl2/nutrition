from flask import render_template,request,redirect,url_for
from . import main
from ..request import post_eggs,post_egg,search_egg

@main.route('/')
def index():
    organic_eggs = post_eggs('organic')
    vegeterian_eggs = post_eggs('vegeterian')
    processed_eggs = post_eggs('processed')
    
    message ="hello world"
    title = "nutrition" 
    search_egg = request.args.get('movie_query')

    if search_egg:
        return redirect(url_for('search',egg_name=search_egg))
    else:

        return render_template('index.html',message = message, title = title, organic = organic_eggs, vegeterian = vegeterian_eggs, processed = processed_eggs)

@main.route('/egg/<int:id>')
def egg(id):
    egg = post_egg(id)
    food_name = f'{egg.food_name}'

    return render_template("egg.html", food_name=food_name, egg=egg)

@main.route('/search/<egg_name>')
def search(egg_name):
    egg_name_list = egg_name.split(" ")
    egg_name_format = "+".join(egg_name_list)
    searched_eggs = search_egg(egg_name_format)
    food_name = f'search results for {egg_name}'

    return render_template('search.html',eggs = searched_eggs)  
