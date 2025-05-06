import openai
import config

openai.api_key = config.OPENAI_API_KEY

def generate_cover(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response["data"][0]["url"]
