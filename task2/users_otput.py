"""Prints chosen item from dictionary"""

def print_dict_items(dct: dict) -> None:
    """
    Prints info about items in dictionary
    Args:
        dct (dict): dictionary
    """
    just_text = []
    objects = []
    print("\n"+"-"*30)
    for key in dct.keys():
        if isinstance(dct[key], dict):
            objects.append(f'"{key}"   -   dict with such keys: {list(dct[key].keys())}')
        elif isinstance(dct[key], list):
            objects.append(f'"{key}"   -   list of {len(dct[key])} elements')
        else:
            just_text.append(f'"{key}"   -   {dct[key]}')
    for elem in just_text + objects:
        print(elem)
    print("-"*30,"\n")
