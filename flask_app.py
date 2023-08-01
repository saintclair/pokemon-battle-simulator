# Import flask and datetime module for showing date and time
from flask import Flask, jsonify
import requests
import datetime
import time
import random

from api.promptlayer.routes import bp_promptlayer
from api.openai.routes import bp_openai

# Initializing flask app
app = Flask(__name__)
 
app.register_blueprint(bp_promptlayer)
app.register_blueprint(bp_openai)

"""
x = datetime.datetime.now()

# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name': "geek",
        "Age": "22",
        "Date": x,
        "programming": "python"
    }
 
@app.route('/time')
def get_current_time():    
    return {'time': time.time()}     
"""

URL_POKEAPI = "https://pokeapi.co/api/v2"

@app.route('/gerar_batalha')
def gerar_batalha():
    pokemon1_id = random.randint(1, 150)
    pokemon2_id = random.randint(1, 150)
    return jsonify({"pokemon1_id": pokemon1_id, "pokemon2_id": pokemon2_id})

@app.route('/resultado_batalha/<int:pokemon1_id>/<int:pokemon2_id>')
def resultado_batalha(pokemon1_id, pokemon2_id):
    # Faça uma requisição à PokeAPI para obter informações sobre os Pokémon usando os IDs.
    r = requests.get(f"{URL_POKEAPI}/pokemon/{pokemon1_id}/")
    pokemon1 = r.json()

    r = requests.get(f"{URL_POKEAPI}/pokemon/{pokemon2_id}/")
    pokemon2 = r.json()

    # Implemente a lógica para determinar o vencedor com base nas características dos Pokémon.
    
    # @TODO: openai
    if pokemon2['base_experience'] > pokemon1['base_experience']:
        loser = pokemon1
        winner = pokemon2
    else:
        loser = pokemon2
        winner = pokemon1

    explanation = f"A base_experience do {winner['name']} é \
        {winner['base_experience']} \
        enquanto do {loser['name']} é {loser['base_experience']}"

    # Retorne os resultados em formato JSON.
    return jsonify({"winner": winner['name'], "explanation": explanation})

# Running app
if __name__ == '__main__':
    app.run(debug=True)
