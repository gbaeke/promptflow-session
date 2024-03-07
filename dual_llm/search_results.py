
from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def search_results(ai_search_results: list) -> str:

    context = ""
    for result in ai_search_results:
        # add name, url, description from result to a string with newlines in between
        context += f"Name: {result['original_entity']['name']}\nUrl: {result['original_entity']['url']}\nDescription: {result['original_entity']['description']}\n\n---\n\n"

    return context
