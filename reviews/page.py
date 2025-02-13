import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'rating': 5
    },
    {
        'id': 2,
        'rating': 4
    },
    {
        'id': 3,
        'rating': 3
    },
]

def show_reviews():
    st.write('Reviews List:')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
    )
