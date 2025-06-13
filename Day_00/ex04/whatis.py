# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 4 *******************

import sys


# on met ici une signature avec annotation de type, optionnelle
def whatis(arg: int) -> int:
    if arg % 2 == 1:
        print("I'm Odd")
    else:
        print("I'm Even")
    return 0


if __name__ == "__main__":
    arguments = sys.argv[1:]  # on recupere les args depuis le terminal avec sys
    # print("Liste des arguments reciup en ligne de terminal : ", arguments)
    if len(arguments) > 1:
        print("AssertionError: more than one argument is provided")
    elif len(arguments) == 1:
        arg = arguments[0]
        try:
            number = int(arg)
            whatis(number)
        except ValueError:
            print("AssertionError: argument is not an integer")
    else:
        pass
