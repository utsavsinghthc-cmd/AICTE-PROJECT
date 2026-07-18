import os
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

# IBM Watsonx Credentials
credentials = Credentials(
    url="https://au-syd.ml.cloud.ibm.com",
    api_key="i9IqZucDcPWkJA972rAmh2inBVFg5ab-E1HZIzjuL1md"
)

# Initialize Model
model = ModelInference(
    model_id="meta-llama/llama-3-3-70b-instruct",
    credentials=credentials,
    project_id="f3b7a411-83bb-48a6-a54c-f78e3d6613ea"
)

prompt = """
You are SmartChef AI.

Suggest an Indian recipe using:
- Potato
- Onion
- Tomato

Return in this format:

Recipe Name:
Preparation Time:
Ingredients:
Cooking Steps:
"""

try:
    response = model.generate_text(
        prompt=prompt,
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 300,
            "temperature": 0.5
        }
    )

    print("\n===== AI RESPONSE =====\n")
    print(response)

except Exception as e:
    print("\n===== ERROR =====\n")
    print(e)