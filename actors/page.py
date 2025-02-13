import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Will Smith'
    },
    {
        'id': 2,
        'name': 'Ana Paula Arosio'
    },
    {
        'id': 3,
        'name': 'Jhonny Depp'
    },
]


def show_actors():
    st.title('Actors/Actresses list:')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )

    st.title('New Actor')
    name = st.text_input('Actor')
    if st.button('Register'):
        st.success(f'Actor/Actress "{name}" registered successfully!')
