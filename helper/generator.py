import os
from dotenv import load_dotenv
import openai

load_dotenv()

TOKEN_AI = os.getenv('TOKEN_AI')
openai.api_key = TOKEN_AI

def generateImage(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url