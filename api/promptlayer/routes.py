from flask import Blueprint, request
import os
import time
import requests
import promptlayer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

# DOCS: https://docs.promptlayer.com/reference/rest-api-reference

promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")
BASE_PROMPT_LAYER_URL = "https://api.promptlayer.com/rest"

bp_promptlayer = Blueprint('promptlayer', __name__)

@bp_promptlayer.route('/track-request', methods=['POST'])
def track_request(request_response, prompt,  prompt_id, prompt_version:int, prompt_input_variables, function_name="openai.Completion.create", engine="text-ada-001", tags=[]):
    _time = time.time()

    request_start_time =  _time # ex:1673987077.463504
    request_end_time = _time # ex: 1673987077.463504

    res = requests.post(
        url=f"{BASE_PROMPT_LAYER_URL}/track-request",
        json={
            "function_name": function_name,            
            "kwargs": { # kwargs will need messages if using chat-based completion
                "engine": engine, 
                "prompt": prompt
            },
            "tags": tags, # ex: ["hello", "world"],
            "request_response": request_response,
            "request_start_time": request_start_time,
            "request_end_time": request_end_time,
            "prompt_id": prompt_id,
            "prompt_input_variables": prompt_input_variables,
            "prompt_version": prompt_version,
            "api_key": promptlayer.api_key,
        }
    )

    return res

@bp_promptlayer.route('/get-prompt-template', methods=['GET'])
def get_prompt_template(promptname:str, promptversion:str):


    response = requests.get(
        f"{BASE_PROMPT_LAYER_URL}/get-prompt-template",
        headers={
            "X-API-KEY": promptlayer.api_key
        }, 
        params={
            "prompt_name": promptname,
            "version": promptversion
        }
    )

    return response

@bp_promptlayer.route('/publish-prompt-template', methods=['POST'])
def publish_prompt_template(prompt_name, prompt_template, tags=None):

    payload={
        "api_key": promptlayer.api_key,
        "prompt_name": prompt_name,
        "version": prompt_template
    }

    if tags:
        payload['tags'] = tags # []

    request_response = requests.post(
        url=f"{BASE_PROMPT_LAYER_URL}/publish-prompt-template",
        json=payload
        
    )

    return request_response

@bp_promptlayer.route('/track-score', methods=['POST'])
def track_score(prompt_name, score, pl_request_id):

    request_response = requests.post(
        f"{BASE_PROMPT_LAYER_URL}/track-score",
        json={
            "request_id": pl_request_id,
            "score": score,
            "api_key": promptlayer.api_key,
        },
    )

    return request_response


@bp_promptlayer.route('/track-prompt', methods=['POST'])
def track_prompt(request_id, version, prompt_name:str, prompt_input_variables = {}):

    prompt_input_variables = {}

    payload = {
        "api_key": promptlayer.api_key,
        "prompt_name": prompt_name,
        "request_id": request_id,
        "prompt_input_variables": prompt_input_variables, #{"variable1": "value1", "variable2": "value2"},
        "version": version
    }

    response = requests.post(
        f"{BASE_PROMPT_LAYER_URL}/track-prompt",
        json=payload
    )

    return response

@bp_promptlayer.route('/track-metadata', methods=['POST'])
def track_metadata(request_id, metadata = {}):

    payload = {
          "api_key": promptlayer.api_key,
          "request_id": request_id,
          "metadata": metadata
    }
    
    response = requests.post(
      f"{BASE_PROMPT_LAYER_URL}/track-metadata",
      json=payload,
    )

    return response

