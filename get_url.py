
from promptflow import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def get_url(image_json: str) -> str:
    url = json.loads(image_json)["url"]

    return url
