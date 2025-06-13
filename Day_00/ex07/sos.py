# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 7 *******************

import sys


def main():

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    else:
        argument = sys.argv[1]
        try:
            for char_test in argument:
                if not char_test.isalnum():
                    print("AssertionError: the arguments are bad")
                    sys.exit(1)
        except Exception as e:
            print(f"AssertionError {e} : the arguments are bad")
            sys.exit(1)

    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "'": ".----.",
        "!": "-.-.--",
        "/": "-..-.",
        "(": "-.--.",
        ")": "-.--.-",
        "&": ".-...",
        ":": "---...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "-": "-....-",
        "_": "..--.-",
        '"': ".-..-.",
        "$": "...-..-",
        "@": ".--.-.",
        " ": "/",
    }
    for letter in argument.upper():
        morse_code = NESTED_MORSE.get(letter, " ")
        print(morse_code, end=" ")
    print()


if __name__ == "__main__":
    main()
