import streamlit as st
from openai import OpenAI
import os

st.title("My Super Awesome OpenAI API Deployment!")

prompt = st.text_input("What is your prompt today?", "Damascus is")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["OpenAIkey"]

### OpenAI stuff: Creative: High temperature
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 1.8,
  max_tokens=20
)

### Display
st.write(
    "Creative: " + response.choices[0].message.content
)


### OpenAI stuff: Predictable: Low temperature
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  temperature = 0.2,
  max_tokens=20
)

### Display
st.write(
    "Predictable: " + response.choices[0].message.content
)
