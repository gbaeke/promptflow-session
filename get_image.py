from promptflow import tool
import json, base64, requests

# no error checking in this code whatsoever :-)

def url_to_base64(image_url):
    response = requests.get(image_url)
    return 'data:image/jpg;base64,' + base64.b64encode(response.content).decode('utf-8')

@tool
def my_python_tool(image_json: str) -> str:
    url = json.loads(image_json)["url"]

    if url:
        base64_string = url_to_base64(url)
    else:
        base64_string = url_to_base64("https://placehold.co/400/jpg?text=No+image")

    return base64_string



    