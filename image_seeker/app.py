from promptflow import load_flow
import streamlit as st
import json
import requests
import base64

# load Prompt Flow from parent folder
flow_path = "../dual_llm"
f = load_flow(flow_path)

# Streamlit UI
st.title('Search for an image')

with st.sidebar:
    use_mistral = st.toggle('Use Mistral', False)

# User input
user_query = st.text_input('Enter your query and press enter:')

if user_query:
    # set engine
    engine = "mistral" if use_mistral else "openai"

    # extract url from dict and wrap in img tag
    flow_result = f(description=user_query, engine=engine)
    print(f)

    results = list(flow_result["results"])
    search_results = flow_result["search_results"]

    # extraxt image and url from results
    url = results[0]
    image = results[1]

    img_tag = f'<a href="{url}"><img src="{image}" alt="image" width="300"></a>'
        
    # just use markdown to display the image
    st.markdown(f"🌆 Image URL: {url}")
    st.markdown(img_tag, unsafe_allow_html=True)

    # retrieve the other images from original_entiry.url in search_results
    st.write("🔍 Other images from the same source:")
    for result in search_results:
        other_url = result["original_entity"]["url"]
        if other_url != url:
            st.markdown(f"🌆 Image URL: {other_url}")
            st.markdown(f'<a href="{other_url}"><img src="{other_url}" alt="image" width="300"></a>', unsafe_allow_html=True)

    # display search results
    st.write("🔍 Search Results:")
    for result in search_results:
        st.write(result)
