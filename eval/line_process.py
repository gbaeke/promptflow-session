# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow import tool
import json


@tool
def line_process(url: str, prediction: str):

    s_url = json.loads(url).get("url")

    # Add your line processing logic here
    processed_result = "Correct" if s_url.lower() == prediction.lower() else "Incorrect"

    return processed_result
