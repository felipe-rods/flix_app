import streamlit as st
from movies.page import show_movies
from genres.page import show_genres
from login.page import show_login
from actors.page import show_actors
from reviews.page import show_reviews


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Select an option',
            ['Home', 'Movies', 'Genres', 'Actors/Actresses', 'Reviews']
        )

        if menu_option == 'Home':
            st.write('Home')

        if menu_option == 'Movies':
            show_movies()

        if menu_option == 'Genres':
            show_genres()

        if menu_option == 'Actors/Actresses':
            show_actors()

        if menu_option == 'Reviews':
            show_reviews()


if __name__ == '__main__':
    main()
