"""Function for getting needed data from dictionary"""

from users_input import get_users_input
from users_otput import print_dict_items
from get_artists_songs import get_most_popular_track

def parse_dict(token: str, dct: dict) -> bool:
    """
    Recursive function for parsing dictionary
    Args:
        token (str): token
        dct (dict): dictionary to parse
    Returns:
        bool: wherter stop recursion
    """
    print_dict_items(dct)
    user_choice = get_users_input(dct)
    if user_choice == "exit":
        return False
    if isinstance(dct[user_choice], list):
        while True:
            i = input(f"Enter index in range (1 - {len(dct[user_choice])}) -> ")
            if i == "exit":
                return False
            if i.isdigit() and int(i) - 1 in range(len(dct[user_choice])):
                i = int(i) - 1
                break
        if isinstance(dct[user_choice][i], dict):
            dct[user_choice] = dct[user_choice][i]
            if i == 0 and user_choice == 'tracks':
                dct[user_choice] = get_most_popular_track(token, dct[user_choice]['name'])['tracks']
        else:
            return False
    elif not isinstance(dct[user_choice], dict):
        print("\n" + "-" * 30 + "\n" + dct[user_choice] + "\n" + "-" * 30 + "\n")
        return False
    parse_dict(token, dct[user_choice])
