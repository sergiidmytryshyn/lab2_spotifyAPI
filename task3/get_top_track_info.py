"""Gets data about artist's top track using his ID"""

import json
import base64
from requests import get, post

def get_token(client_id: str, client_secret: str) -> str:
    """
    Gets token
    Args:
        client_id (str): client id
        client_secret (str): client secret
    Returns:
        str: access token
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data,timeout=10)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token: str) -> str:
    """Gets header"""
    return {"Authorization": "Bearer " + token}

def search_for_artist(token: str, artist_name: str) -> str:
    """
    Gets artist's ID
    Args:
        token (str): token
        artist_name (str): artist name
    Returns:
        str: artist's ID
    """
    headers = get_auth_header(token)
    query_url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    result = get(query_url, headers=headers, timeout=10)
    try:
        json_result = json.loads(result.content)["artists"]["items"]
        artist_id = json_result[0]
    except (IndexError, KeyError):
        return None
    return artist_id

def get_top_track(token: str, artist_id: str) -> dict:
    """
    Gets data about artist's top tracks
    Args:
        token (str): token
        artist_id (str): artist's ID
    Returns:
        dict: top track info
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers, timeout=10)
    json_result = json.loads(result.content)['tracks'][0]['name']
    return json_result
