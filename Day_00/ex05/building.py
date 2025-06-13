import sys


def main():
    if len(sys.argv) > 2:
        print("Assertion Error: argument is not a string")
        sys.exit(1)
    elif len(sys.argv) == 1:
        sys.exit(1)
    else:
        string = sys.argv[1]
        if not isinstance(string, str):
            print("Assertion Error: argument is not a string")
            sys.exit(1)
    nb_char = nb_up = nb_low = nb_digit = nb_space = nb_punct = 0
    nb_char = len(string)

    for letter in string:
        if letter.isupper():
            nb_up += 1
        elif letter.islower():
            nb_low += 1
        elif letter.isdigit():
            nb_digit += 1
        elif letter.isspace():
            nb_space += 1
        else:
            nb_punct += 1
    print(
        "The text contains ",
        nb_char,
        " characters:\n",
        nb_up,
        " upper letters\n",
        nb_low,
        " lower letters\n",
        nb_punct,
        " punctuation marks\n",
        nb_space,
        " spaces\n",
        nb_digit,
        " digits",
    )


if __name__ == "__main__":
    main()
# inutile ici de passer un argument au main, il sera recupéré par sys.argv
