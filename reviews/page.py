import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewService
from st_aggrid import AgGrid


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.title('Reviews list:')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            key='reviews_grid',
        )
    else:
        st.warning('No reviews found.')

    st.title('New Review')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Movie', list(movie_titles.keys()))

    rating = st.number_input(
        label='Rating',
        min_value=1,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comment')

    if st.button('Register'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            rating=rating,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Register error. Verify the fields.')
