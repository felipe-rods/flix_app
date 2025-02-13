import streamlit as st


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

    st.table(genres)

    st.title('New Genre')
    name = st.text_input('Genre')
    if st.button('Register'):
        st.success(f'New "{name}" genre registered successfully!')
