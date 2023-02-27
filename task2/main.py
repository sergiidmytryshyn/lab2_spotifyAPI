"""Lab2 task2 Main Function"""

import os
from dotenv import load_dotenv
from get_artists_songs import get_token, get_songs_by_artist, search_for_artist
from get_data_from_json import parse_dict

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def main() -> None:
    """Main function"""
    print('You must choose first track in "tracks" to get info about available_markets')
    print('Print "exit" anytime you want to stop this')
    run = True
    while run:
        token = get_token(client_id, client_secret)
        artist_name = input("Input artist's name:\n")
        result = search_for_artist(token, artist_name)
        if result:
            artists_id = result['id']
            top_songs_data = get_songs_by_artist(token, artists_id)
            run = parse_dict(token, top_songs_data)

if __name__ == "__main__":
    main()
