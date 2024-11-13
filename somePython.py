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
      ### CONTEXT ####
      I am the moderator of a financial social media engine focusing on stock trading. The following post have been reported by other users as violating the social media guidelines.
  
      ### OBJECTIVE ####
      Determine whether the post is violating the guidelines, if the post is violating the guidelines it should be removed, if not it must not be removed.
  
      ### SOCIAL MEDIA GUIDELINES ####
      - A: comply with all applicable laws and regulations when using Shareville and that not use Shareville to perform any illegal, deceptive, harmful or discriminatory act.
      - B: ensure that its actions on Shareville do not constitute or may be deemed to constitute dissemination of false or misleading information which may involve undue market influence according to law (2016:1307) on penalties for market abuse when trading in financial instruments and not to make available inside information or otherwise act with the aim of unduly influence the valuation of a financial instrument. Spread of false or misleading information can have a significant impact on prices on financial instruments in a relatively short time. It could be about fabrication of obviously false information, but also of deliberate omission of material facts, as well as knowingly misreporting information.
      - C: ensure that the posts that the User contributes to Shareville do not have such content that they constitute investment recommendations or other information which recommends or suggests an investment strategy regarding a or several financial instruments according to the regulation of the European Parliament and the Council (EU) 596/2014 and Commission Delegated Regulation (EU) 2016/958 (market abuse), unless the User has received in writing permission from Shareville to publish such content. This means for example, posts with direct recommendations or invitations on investments in financial instruments and proposals, such as "buy", "hold" or "sell", are not permitted.
      - D: not provide personal recommendations about investments in financial instruments to other Users (investment advice).
      - E: refrain from personal attacks, aggressive statements, insults, racist or sexist views, posts that have no relevance to Shareville as well as statements that may appear offensive.
      - F: not post content that is hateful, threatening, pornographic or the like incites acts of violence or violates the provisions of applicable f regulations such as the Data Protection Regulation or the law (1998:112) on liability for electronic bulletin boards.
      - G: not contribute material, or link to material, that may infringe someone else's rights or is otherwise in conflict with the law or another's right.
      - H: not obtain or attempt to obtain access to other Users' credentials or prepare or attempt to prepare improper access to connected networks or data resources, or unauthorized access to, use, destroy, distort or forward information from such source.
      - I: not collect User Content or data, or otherwise obtain access to Shareville via automated means (e.g. robots, spiders or scrapers) without Shareville's permission.
      - J: not upload viruses or other malicious code or take any action that may disable, overburden or impair Shareville's functionality.
      - K: not without the written consent of Shareville advertise or for commercial purposes advertise your own or others' services.
  
      ### REPORTED SOCIAL MEDIA POST ####
      {social_media_post}
  
      ### RESPONSE ####
      Output with a rationale text and provide which guidelines the post is violating and a violating ratio from 0 to 100 to what extent the post is violating guidelines on the json format {{"rationale": string, "violationRatio": int}}.
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

