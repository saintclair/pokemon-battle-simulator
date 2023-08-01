from api.openai.routes import completion_create

def determine_winner(pokemon1, pokemon2):
    if pokemon2['base_experience'] > pokemon1['base_experience']:
        return pokemon2, pokemon1
    return pokemon1, pokemon2

def analyze_battle(winner, loser):
    p_name1 = winner['name']
    p_name2 = loser['name']

    #max_characters = 1000

    prompt = f"""
    You are about to witness an exciting Pokémon battle between {p_name1} e {p_name2}! 
    Let's take a detailed look at each Pokémon's attributes, types, and moves to understand how the winner was decided.

    {p_name1} It's a Pokémon of the type {winner['types'][0]['type']['name']} com 
    {winner['base_experience']} base experience points. Its stats are as follows:
    - Statistic: {winner['stats'][0]['base_stat']}
    - And other relevant attributes.

    {p_name2} It's a Pokémon of the type {loser['types'][0]['type']['name']} com 
    {loser['base_experience']} base experience points. Its stats are as follows:
    - - Statistic: {loser['stats'][0]['base_stat']}
    - And other relevant attributes.

    Now, let's look at each Pokémon's moves and how they fared in battle. 
    (Add information about the moves used and their effects)

    (Add details about the advantages and disadvantages of Pokémon types and how this influenced the battle)

    After an intense battle, {p_name1} emerged as the winner! His combination of attributes and well-planned strategy gave him victory over {p_name2}. 
    Congratulations to the trainer of the winning Pokémon on his brilliant victory!
    """
    #Summarize in a maximum of {max_characters} characters

    explanation = completion_create(prompt, pl_tags=[
        'battle',
        f'winner:{p_name1}', 
        f'loser:{p_name2}'])

    return explanation