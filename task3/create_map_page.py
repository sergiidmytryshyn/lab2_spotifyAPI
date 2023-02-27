"""Main Function that creates page with map"""

import os
from dotenv import load_dotenv
from get_top_track_info import get_token, get_top_track, search_for_artist
from get_available_markets import get_available_markets, get_markets_names
from create_map import create_map

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def create_map_page(artist_name: str) -> bool:
    """Main function"""
    token = get_token(client_id, client_secret)
    result = search_for_artist(token, artist_name)
    if not result:
        return False
    artists_id = result['id']
    top_track_name = get_top_track(token, artists_id)
    markets = get_available_markets(token, top_track_name)
    markets_names = get_markets_names(markets)
    create_map(markets_names)
    return True
