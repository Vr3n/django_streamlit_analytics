from streamlit.elements.widgets.number_input import Number
from urllib.parse import uses_fragment
import streamlit as st
import plotly.io as pio
import plotly.express as px
import numpy as np
import requests
import pandas as pd


swapi_endpoint = "https://swapi.dev/api/people/"
api_url = "http://127.0.0.1:8000/api/customers"

# fetching the data.
def fetch_data(endpoint: str):
	response = requests.get(endpoint)
	data = response.json()
	return data

def send_data(name: str, gender: str | None, age: Number, favorite_number: Number):
	gender_val = "0" if gender == "Female" else "1"

	data = {
		"name": name,
		"gender": gender_val,
		"age": age,
		"favorite_number": favorite_number,
	}

	res = requests.post(api_url, json=data)
	return res


pio.templates.default = "seaborn"

st.title("Analytics Dashboard")
st.write("v.0.01")

# Layout Customization.
col_1, col_2 = st.columns(2)

with col_1:
	st.header("Column 1")
	st.write("Some content to fill here.")
	st.write(st.session_state.counter)

	with st.expander("Click to choose something!"):
		st.write("Option to choose")
		st.write("Another option to choose")

with col_2:
	st.header("Column 2")
	categories = ["A", "B", "C", "D"]
	values = np.random.randint(10, 100, size=(4,))

	fig = px.bar(x=categories,y=values, title="Test Chart")
	st.plotly_chart(fig, use_container_width=True)


# session state.
if 'counter' not in st.session_state:
	st.session_state.counter = 0

# increment buton.
if st.button('increment'):
	st.session_state.counter += 1


# Data from swapi api.

swapi_data = fetch_data(swapi_endpoint)

if swapi_data:
	df = pd.DataFrame(swapi_data['results'])

	st.dataframe(df)


# Data from our database.
st.write("## Customers")

api_data = fetch_data(api_url)

if api_data:
	df = pd.DataFrame(api_data)

	scatter_fig = px.scatter(df, x="age", y="favorite_number")

	st.plotly_chart(scatter_fig, use_container_width=True)


# Form to collect customer data.
st.write("## Customer Form.")

name=st.text_input("You name")
gender=st.radio("Select your gender", ["Male", "Female"])
age=st.slider("Select your age", 0, 100, 8)
favorite_number = st.number_input("Enter your favorite number", step=1)

if st.button("Submit"):
	res = send_data(name, gender, age, favorite_number)

	if res.status_code == 200:
		st.success("New customer data created!")
		st.rerun()
	else:
		st.error("Something went wrong!")