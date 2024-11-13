from google.colab import auth
auth.authenticate_user()

import pandas as pd

from google.cloud import bigquery
import vertexai
from vertexai.preview.generative_models import GenerativeModel

# Authentication and client setup
client = bigquery.Client(project='prod-sandbox-34938')
vertexai.init(project='prod-data-science-10722')

model = GenerativeModel("gemini-1.5-flash-001")

def get_promt(social_media_post):
    return f"""
           """
  

def generate(promptText):
    responses = model.generate_content(
      promptText,
      generation_config={
          "max_output_tokens": 2048,
          "temperature": 0.0,
          "top_p": 1.0,
          "response_mime_type": "application/json"
      },
      safety_settings=[],
    stream=True,
    )
  
    return_string = ''
    for response in responses:
        return_string += response.text
  
    return return_string

prompt = get_promt("tror også den stiger i morgen:)")
prompt

prediction = generate(prompt)
prediction

