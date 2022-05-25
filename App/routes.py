from app import app
from flask import render_template, request
import requests as r
from .services import Pokemon




@app.route('/')
def home():

    data = r.get(f'https://pokeapi.co/api/v2/pokemon/entei')
    if data.status_code == 200:
        data = data.json()

    my_pokemon = Pokemon(data)

    return render_template('main_page.html', my_pokemon=my_pokemon)

#Donovan, You need to refactor this. This is not good code.
@app.route('/', methods=['POST', 'GET'])
def home_post():
    try:
        text = request.form['text']
        lower_text = text.lower()

        data = r.get(f'https://pokeapi.co/api/v2/pokemon/{lower_text}')
        if data.status_code == 200:
            data = data.json()

        my_pokemon = Pokemon(data)

        return render_template('main_page.html', my_pokemon=my_pokemon)
    except TypeError:
        lower_text = 'entei'
        data = r.get(f'https://pokeapi.co/api/v2/pokemon/{lower_text}')
        if data.status_code == 200:
            data = data.json()

        my_pokemon = Pokemon(data)
        my_pokemon.name = 'ERROR ERROR NO POKEMON WITH THAT NAME EXISTS. PLEASE TRY AGAIN'
        return render_template('main_page.html', my_pokemon=my_pokemon)




@app.route('/regions', methods=['POST', 'GET'])
def regions():
    try:
        region_list = ['kanto', 'johto', 'hoenn', 'sinnoh', 'unova', 'kalos', 'alola', 'galar']
        region_string = "Which region would you like to see? Here is a list: \nkanto\njohto\nhoenn\nsinnoh\nunova\nkalos\nalola\ngalar\n"

        reg_text = request.form['reg_text']
        try: 
            reg_range = request.form['reg_range']
            reg_range = tuple(map(int, reg_range.split(', ')))
        except: 
            reg_range =(0,30)

        for i in range(len(region_list)):
            if reg_text == region_list[i]:
                ind = i + 1

        data = r.get(f'https://pokeapi.co/api/v2/generation/{ind}/')
        if data.status_code == 200:
            data = data.json()

        poke_list = []
        for x in range(reg_range[0], reg_range[1]):
            y=data['pokemon_species'][x]['name']
            poke_list.append(y)
        
        return render_template('regions.html', region_list=region_list, region_string=region_string, ind=ind, poke_list=poke_list, reg_text=reg_text)
    except KeyError:
        region_list = ['kanto', 'johto', 'hoenn', 'sinnoh', 'unova', 'kalos', 'alola', 'galar']
        region_string = "Which region would you like to see? Here is a list: \nkanto\njohto\nhoenn\nsinnoh\nunova\nkalos\nalola\ngalar\n"
        ind = 1
        reg_text = region_list[0]
        data = r.get(f'https://pokeapi.co/api/v2/generation/{ind}/')
        if data.status_code == 200:
            data = data.json()

        try: 
            reg_range = request.form['reg_range']
            reg_range = tuple(map(int, reg_range.split(', ')))
        except: 
            reg_range =(0,30)

        poke_list = []
        for x in range(reg_range[0], reg_range[1]):
            y=data['pokemon_species'][x]['name']
            poke_list.append(y)
        
        return render_template('regions.html', region_list=region_list, region_string=region_string, ind=ind, poke_list=poke_list, reg_text=reg_text)
