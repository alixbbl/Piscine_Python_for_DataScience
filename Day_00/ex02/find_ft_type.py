# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 2 *******************

def all_thing_is_obj(object):
    if isinstance(object, list):
        print("List : <class 'list'>")
    elif isinstance(object, tuple):
        print("Tuple : <class 'tuple'>")
    elif isinstance(object, set):
        print("Set : <class 'set'>")
    elif isinstance(object, dict):
        print("Dict : <class 'dict'>")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        return ("Type not found\n42")