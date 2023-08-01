from flask import Blueprint
import json
import requests
#import openai
import promptlayer
#from api.promptlayer.routes import track_request

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('.env')

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.getenv("OPENAI_API_KEY")

bp_openai = Blueprint('openai', __name__)

@bp_openai.route('/completion-create', methods=['POST'])
def completion_create(prompt, pl_tags=[], engine="text-davinci-003"):

    """
    Using OpenAI sem promptlayer here

    # Do something fun 🚀
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        "Authorization": f"Bearer {openai.api_key}", 
        "Content-Type": "application/json"
    }

    body = {
        "model": engine,
        "messages":[
            {
                "role": "user",
                "content": prompt
            }
        ],
        "pl_tags": pl_tags
    }

    r = requests.post(url, 
                headers=headers, 
                data=json.dumps(body))

    response = r.json()

    # try:
    #     prompt_id = ""
    #     prompt_version = 1
    #     prompt_input_variables = {}

    #     # @TODO: check documentation promptlayer
    #     track_request(request_response, 
    #                 prompt, 
    #                 prompt_id, 
    #                 prompt_version:int, 
    #                 prompt_input_variables, 
    #                 function_name="openai.Completion.create",
    #                 engine=engine, 
    #                 tags=[])
    # except Exception as e:
    #     print(f'{e}')
    
    if 'error' in response:
        # @TODO: tratar quando quebrar um nova requisicao talvez
        return 'OPEN AI Error:' + response['error']['message']
    
    return response["choices"][0]["message"]['content']
    """

    # Using Prompt Layer
    response = openai.Completion.create(
        engine="text-davinci-003", #gpt-3.5-turbo (not working in promptlayer)
        prompt=prompt, 
        pl_tags=pl_tags
    )

    #return response["choices"][0]["message"]['content']
    return response["choices"][0]["text"]
