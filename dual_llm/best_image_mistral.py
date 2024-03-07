
from promptflow import tool
from promptflow.connections import CustomConnection
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage



# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def best_image(prompt: str, mistral: CustomConnection) -> str:
    
    groq_dict = dict(mistral)
    mistral_endpoint = groq_dict['endpoint']
    mistral_key = groq_dict['key']
    mistral_model = groq_dict['model']

    client = MistralClient(api_key=mistral_key, endpoint=mistral_endpoint)

    try:
        chat_response = client.chat(
            model=mistral_model,
            response_format={"type": "json_object"},
            messages=[ChatMessage(role="user", content=prompt)]
        )

        return chat_response.choices[0].message.content
    except:
        return None