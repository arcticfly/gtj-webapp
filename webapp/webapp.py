import streamlit as st
import pandas as pd
import numpy as np
import requests
import json


INITIAL_INPUT_TEXT="Horseback riding"
INITIAL_QUESTIONS_TEXT="Which tags apply to this activity? How long does it usually take in minutes? How would you rate the cost and energy level on a scale from 1 to 10?"
INITIAL_SAMPLE_JSON='{"outdoors": boolean, "indoors": boolean, "duration": integer, "cost": integer, "energy": integer}'

st.title('GPT to JSON')

# @st.cache
def get_json(input_text: str, questions: str, sample_json: str):
    try:
        r = requests.post('https://gpt-to-json.loca.lt/generate-json', json={'text': input_text, 'questions': questions, 'json': sample_json})
        print("r", r)
        print('r.json', r.json())
        return r.json()
    except:
        return 'Failed to fetch json'

def cannot_get_json(input_text: str, questions: str, sample_json: str):
    if not input_text or input_text == '':
        return True
    if not questions or questions == '':
        return True
    if not sample_json or sample_json == '':
        return True
    return False


input_text = st.text_area("Input text", value=INITIAL_INPUT_TEXT, max_chars=None, key=None, placeholder="We the people, in order to form...", label_visibility="visible")
questions = st.text_area("Questions", value=INITIAL_QUESTIONS_TEXT, max_chars=None, key=None, placeholder="What tags are associated with this text? How would you rate its energy level on a scale from 1 to 10?", label_visibility="visible")
sample_json = st.text_area("Sample JSON", value=INITIAL_SAMPLE_JSON, max_chars=None, key=None, placeholder='{{ "confident": boolean, "intellectual": boolean, "goofy": boolean, "energy_level": number}}.', label_visibility="visible")

displayed_json = st.text('Generating json...')

json_object = json.loads(get_json(input_text, questions, sample_json))

displayed_json = st.text(json.dumps(json_object, indent=2))

