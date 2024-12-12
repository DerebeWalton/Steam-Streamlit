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

    topgames = df.sort_values(sort_by, ascending=False)
    
    fig = px.bar(topgames, x='name', y=sort_by)

    return fig

# top_games_plot(df=pd.read_csv('steam_data.csv'))


def single_game_info(df, game="Portal"):
    game_data = df[df['name'] == game].copy()
    appid = game_data['appid']
    total_playtime = game_data['playtime_forever']

    output = pd.DataFrame({
        "Game Title": game,
        "Steam appID": appid,
        "Total Playtime": total_playtime
    })

    return output

