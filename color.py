#import google.generativeai as palm
# STreamlit http://localhost:8501/
#API_KEY = 'AIzaSyAt8JwfnFsMbaoSsdaPoZ1H3qPqpwBg7vc'
#palm.configure(api_key=API_KEY)

import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


API_KEY = 'AIzaSyAt8JwfnFsMbaoSsdaPoZ1H3qPqpwBg7vc'
genai.configure(api_key=API_KEY)


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    to_markdown(m.name)
     

model = genai.GenerativeModel('gemini-pro')

##%%time
import time
start_time = time.time()

# Your code here
#input_text = model.generate_content("What is colors for well-lit medical student study rooms")
#end_time = time.time()
#execution_time = end_time - start_time
#print(f"Execution time: {execution_time} seconds")

#to_markdown(input_text.text)


response = model.generate_content(["Write a recommendation color for laundry website."], stream=True)
response.resolve()
to_markdown(response.text)


#Streamlit

import streamlit as st

st.title("Text Generation for Web Developer Color Suggestions")

input_text = st.text_input("Enter the text to be used for generating questions")

if st.button("Generate Question"):
    with st.spinner("Generating..."):
        output_text = response(model, input_text)       #error??
        st.write(output_text)