"""Gets data about artists top tracks using his ID"""

import base64
import json
from requests import post, get

def get_token(client_id: str, client_secret: str) -> str:
    """
    Gets token
    Args:
        client_id (str): clients id
        client_secret (str): clients secret
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
    """
    Gets header
    Args:
        token (str): token
    Returns:
        str: header
    """
    return {"Authorization": "Bearer " + token}

def search_for_artist(token: str, artist_name: str) -> str:
    """
    Gets artist's ID
    Args:
        token (str): token
        artist_name (str): artists name
    Returns:
        str: artist's ID
    """
    headers = get_auth_header(token)
    query_url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    result = get(query_url, headers=headers, timeout=10)
    json_result = json.loads(result.content)["artists"]["items"]
    try:
        json_result = json.loads(result.content)["artists"]["items"]
        artist_id = json_result[0]
    except (IndexError, KeyError):
        print('No such artist')
        return None
    return artist_id

def get_songs_by_artist(token: str, artist_id: str) -> dict:
    """
    Gets data about artist's top tracks
    Args:
        token (str): token
        artist_id (str): artist's ID
    Returns:
        dict: top 10 artist's tracks data
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers, timeout=10)
    json_result = json.loads(result.content)
    return json_result

def get_most_popular_track(token: str, track_name: str) -> dict:
    """
    Gets data about most popular artist's track
    Args:
        token (str): token
        track_name (str): track name
    Returns:
        dict: dictionary with most popular artists track data 
    """
    url = f"https://api.spotify.com/v1/search?q={track_name}&type=track&limit=1"
    headers = get_auth_header(token)
    result = get(url, headers=headers, timeout=10)
    json_result = json.loads(result.content)
    return json_result
