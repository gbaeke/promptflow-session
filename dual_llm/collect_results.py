
from promptflow import tool
import json, base64, requests


def url_to_base64(image_url):
    response = requests.get(image_url)
    return 'data:image/jpg;base64,' + base64.b64encode(response.content).decode('utf-8')

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def collect_results(openai_image_json: str, mistral_image_json) -> list:
    image_json=openai_image_json if openai_image_json else mistral_image_json

    # extract url
    url = json.loads(image_json)["url"]

    # get base64 image
    if url:
        base64_image = url_to_base64(url)
    else:
        base64_image = url_to_base64("https://placehold.co/400/jpg?text=No+image")

    return [url, base64_image]