import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def top_games_plot(df, num_games=5, device='All'):
    sort_by = 'playtime_forever'
    if device == 'Windows':
        sort_by = 'playtime_windows_forever'
    elif device == "Steam Deck":
        sort_by = 'playtime_deck_forever'

    topgames = df.sort_values(sort_by, ascending=False).head(num_games)
    
    fig = px.bar(topgames, x='name', y=sort_by)

    return fig



def single_game_info(df, game="Portal"):
    game_data = df[df['name'] == game].copy()
    
    appid = game_data['appid']
    total_playtime = game_data['playtime_forever']
    deck_playtime = game_data['playtime_deck_forever']
    windows_playtime = game_data['playtime_windows_forever']

    output = pd.DataFrame({
        "Game Title": game,
        "Steam appID": appid,
        "Total Playtime": total_playtime,
        "Steam Deck Playtime": deck_playtime,
        "Windows Playtime": windows_playtime
    })

    return output

def single_game_plot(df, game="Portal"):
    game_data = df[df['name'] == game].copy()

    device_time = [game_data['playtime_windows_forever'], game_data['playtime_deck_forever']]
    device_labels = ["Windows", "Steam Deck"]

    fig = px.pie(device_time, labels=device_labels, title=f'Proportions of Devices Playtime for {game}')

    return fig

single_game_plot(df=pd.read_csv('steam_data.csv'), game='Portal 2')