import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Action'
    },
    {
        'id': 2,
        'name': 'Sci-fi'
    },
    {
        'id': 3,
        'name': 'Drama'
    },
]


def show_genres():
    st.write('Genres List:')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
    )

    st.title('New Genre')
    name = st.text_input('Genre')
    if st.button('Register'):
        st.success(f'New "{name}" genre registered successfully!')
