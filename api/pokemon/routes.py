from flask import Blueprint, Request

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('.env')

openai.api_key = os.getenv("OPENAI_API_KEY")

bp_openai = Blueprint('openai', __name__)

@bp_openai.route('/completion-create', methods=['POST'])
def completion_create(prompt, engine="text-ada-001", pl_tags=[]):

    # Do something fun 🚀
    request_response = openai.Completion.create(
        engine, 
        prompt, 
        pl_tags # ex:["name-guessing", "pipeline-2"]
    )

    return track_request(request_response)
