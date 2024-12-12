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

    windows = int(game_data['playtime_windows_forever'].values[0])
    deck = int(game_data['playtime_deck_forever'].values[0])
    unknown = int(game_data['playtime_forever'].values[0]) - windows - deck

    device_time = [windows, deck, unknown]
    print(device_time)
    device_labels = ["Windows", "Steam Deck", 'Unknown']

    fig = px.pie(values=device_time, names=device_labels, title=f'Proportions of Device Playtime for {game}')

    return fig

single_game_plot(df=pd.read_csv('steam_data.csv'), game='Magicka')