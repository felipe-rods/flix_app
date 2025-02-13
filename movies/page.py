import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Pacific Rim'
    },
    {
        'id': 3,
        'name': 'The Godfather'
    },
]


def show_movies():
    st.write('Movies List:')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )
