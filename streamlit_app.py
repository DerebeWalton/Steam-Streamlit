import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from my_plots import *
import streamlit as st

@st.cache_data
def load_steam_data():
    steam_file = 'steam_data.csv'
    df = pd.read_csv(steam_file)
    return df

@st.cache_data
def single_game(df):
    print(single_game_info(df))
    return single_game_info(df)

st.title('Gimotac\'s Games')

data = load_steam_data()

with st.sidebar:
    input_game = st.text_input('Enter a game title (Try Portal!):')
    n_games = st.radio('Top ___ Games', [5,10,20])
    input_device = st.segmented_control("Filter played games by device", ['All', 'Windows', 'Steam Deck'])

tab1, tab2, tab3 = st.tabs(['Full Library', 'Individual Game', 'Data'])

with tab1:
    fig1 = top_games_plot(data, n_games, input_device)
    st.plotly_chart(fig1)
    expander = st.expander("Chart Explanation")
    expander.write('''
                   The chart above shows the top played games on the account given a device. We sort from highest to lowest minutes played on each device.
                   ''')

with tab2:
    fig2 = single_game_info(df=data, game=input_game)
    st.dataframe(fig2)

    fig3 = single_game_plot(df=data, game=input_game)
    st.plotly_chart(fig3)

    expander = st.expander("Note on data")
    expander.write('''
                   Some games may reflect no playtime on one device or another, or even no playtime at all due to much of the game library not having been played.
                   ''')

with tab3:
    st.write('''
             For convenience, here is the dataset we are using
             ''')
    st.dataframe(data)