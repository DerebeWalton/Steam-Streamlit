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
    input_game = st.text_input('Enter a game title:')
    n_games = st.radio('Top ___ Games', [5,10,20])
    input_device = st.segmented_control("Filter played games by device", ['All', 'Windows', 'Steam Deck'])

tab1, tab2 = st.tabs(['Full Library', 'Individual Game'])

with tab1:
    fig1 = top_games_plot(data, n_games, input_device)
    st.plotly_chart(fig1)

with tab2:
    game_data = data[data['name'] == input_game].copy()