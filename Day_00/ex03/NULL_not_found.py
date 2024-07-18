# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 3 *******************
import math
def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : None <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese: nan <class 'float'>")
        return 0
    elif isinstance(object, int) and object == 0 and not isinstance(object, bool):
        print("Zero: 0 <class 'int'>")
        return 0
    elif isinstance(object, str) and object == "":
        print("Empty: <class 'str'>")
        return 0
    elif isinstance(object, bool) and object == False:
        print("Fake: False <class 'bool'>")
        return 0
    else:
        print("Type not found")
        return 1