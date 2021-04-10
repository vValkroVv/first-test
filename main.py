import streamlit as st
import pandas as pd

df = pd.DataFrame({'x': [10, 20, 30, 40],
                   'y': [100, 200, 300, 400],
                   'name': ['alpha', 'beta', 'gamma', 'delta']})

x_max = st.slider('Max value of x', float(df['x'].max()))

st.markdown(""" Let's look""")

st.title("My streamlit app 3ih")
st.title("Git")
df