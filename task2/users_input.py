"""Takes and validates user's input"""

def get_users_input(dct: dict) -> str:
    """
    Takes users input and checks it
    Args:
        dct (dict): checks validity of users input
    Returns:
        str: user's choice
    """
    while True:
        users_choice = input("Select one of the above: ")
        if users_choice == "exit":
            return "exit"
        if users_choice in dct.keys():
            return users_choice
