from flask import Flask, jsonify
import requests
import random

from api.promptlayer.routes import bp_promptlayer
from api.openai.routes import bp_openai
from api.battle_analyzer import analyze_battle, determine_winner

app = Flask(__name__)
app.register_blueprint(bp_promptlayer)
app.register_blueprint(bp_openai)

URL_POKEAPI = "https://pokeapi.co/api/v2"

# Generate 2 numbers between 1 and 150, range offering by PokeAPI
@app.route('/generate_battle')
def generate_battle():
    pokemon1_id = random.randint(1, 150)
    pokemon2_id = random.randint(1, 150)
    return jsonify({"pokemon1_id": pokemon1_id, "pokemon2_id": pokemon2_id})

@app.route('/battle_result/<int:pokemon1_id>/<int:pokemon2_id>')
def battle_result(pokemon1_id, pokemon2_id):
    pokemon1 = get_pokemon_info(pokemon1_id)
    pokemon2 = get_pokemon_info(pokemon2_id)

    winner, loser = determine_winner(pokemon1, pokemon2)
    explanation = analyze_battle(winner, loser)

    return jsonify({"winner": winner['name'], "explanation": explanation})

# Get information from PokeAPI
def get_pokemon_info(pokemon_id):
    r = requests.get(f"{URL_POKEAPI}/pokemon/{pokemon_id}/")
    r.raise_for_status()  # Check errors of API
    return r.json()

if __name__ == '__main__':
    app.run(debug=True)