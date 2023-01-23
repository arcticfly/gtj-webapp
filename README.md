# gtj-webapp

## Introduction

This app is a simple proof of concept that demonstrates the ability of GPT-3 to extract useful information from text and answer provided questions in the form of JSON. Since JSON is readable by machines, a similar app could expose an API that is queryable by any server to answer questions about a given body of text in a way that the calling server could define and understand.

## Running the app

1. Install poetry on your machine if you haven't already.
2. Run `poetry install` in the root directory to install all python packages this project depends on.
3. Run `poetry run streamlit run ./webapp/webapp.py` and you should be good to go!

## Example

To see a running instance of this app, check out [this example](https://arcticfly-gtj-webapp-webappwebapp-gurcy6.streamlit.app/).