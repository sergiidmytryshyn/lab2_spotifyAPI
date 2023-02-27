"""Gets set of top track's available markets countries names"""

import json
from requests import get
from pycountry import countries
from get_top_track_info import get_auth_header

def get_available_markets(token: str, track_name: str) -> list:
    """Gets list of top track's available markets"""
    url = f"https://api.spotify.com/v1/search?q={track_name}&type=track&limit=1"
    headers = get_auth_header(token)
    result = get(url, headers=headers, timeout=10)
    json_result = json.loads(result.content)
    return json_result["tracks"]['items'][0]['available_markets']

def get_markets_names(markets: list) -> set:
    """Takes ISO2 of available markets and returns countries' full names"""
    markets_names = set()
    for country in list(countries):
        if country.alpha_2 in markets:
            markets_names.add(country.name)
    return markets_names
