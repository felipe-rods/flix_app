import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()
    if genres:
        st.write('Genres List:')
        genres_pd = pd.json_normalize(genres)
        AgGrid(
            data=genres_pd,
            key='genres_grid',
        )
    else:
        st.warning('No genre found.')
    
    st.title('New Genre:')
    name = st.text_input('Genre')
    if st.button('Register'):
        new_genre = genre_service.create_genre(
            name=name
        )
        if new_genre:
            st.rerun()
        else:
            st.error('Register error. Verify the field.')
