import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.title('Actors/Actresses list:')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key='actors_grid',
        )
    else:
        st.warning('No actors or actresses found')

    st.title('New Actor')
    name = st.text_input('Actor')
    birthday = st.date_input(
        label='Birthday',
        value=datetime.today(),
        min_value=datetime(1880, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    country_dropdown = [
        'UNITED STATES',
        'BRAZIL',
        'SPAIN',
        'FRANCE',
        'MEXICO',
        'ARGENTINA',
        'UNITED KINGDOM',
        'SOUTH AFRICA',
        'INDIA',
        'HONG KONG',
        'ISRAEL',
        'AUSTRALIA',
        'CANADA',
        'IRELAND',
        'KENYA',
        'EGYPT',
        'SWEDEN',
    ]
    country = st.selectbox(
        label='Country',
        options=country_dropdown
    )
    if st.button('Register'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            country=country,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Register error. Verify the fields.')
