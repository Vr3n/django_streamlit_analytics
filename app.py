import streamlit as st
import plotly.io as pio
import plotly.express as px
import numpy as np

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