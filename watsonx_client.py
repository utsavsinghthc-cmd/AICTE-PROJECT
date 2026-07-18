import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

credentials = Credentials(
    url=os.getenv("https://au-syd.ml.cloud.ibm.com"),
    api_key=os.getenv("i9IqZucDcPWkJA972rAmh2inBVFg5ab-E1HZIzjuL1")
)

model = ModelInference(
    model_id=os.getenv("meta-llama/llama-3-3-70b-instruct"),
    credentials=credentials,
    project_id=os.getenv("f3b7a411-83bb-48a6-a54c-f78e3d6613ea")
)


def generate_recipe(user_prompt):

    prompt = f"""
You are SmartChef AI.

The user will provide available ingredients.

Generate a recipe in this format:

Recipe Name

Preparation Time

Ingredients

Cooking Steps

Cooking Tips

User Ingredients:
{user_prompt}

Only answer in recipe format.
"""

    response = model.generate_text(
        prompt=prompt,
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 400,
            "temperature": 0.4
        }
    )

    return response