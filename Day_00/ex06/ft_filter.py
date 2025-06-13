# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 6a *******************
import sys


def ft_filter(function, seq):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return [item for item in seq if item]
    else:
        return [item for item in seq if function(item)]


def main():

    if len(sys.argv) != 3:
        sys.exit(1)

    function = sys.argv[1]
    if function.lower() == "none":
        function = None
    else:
        try:
            function = eval(function)
        except Exception as e:
            print(e)
            sys.exit(1)

    try:
        seq = sys.argv[2].split(",")
    except Exception as e:
        print(e)
        sys.exit(1)

    result = ft_filter(function, seq)
    print(result)


if __name__ == "__main__":
    main()


# Comment recuperer et ouvrir un fichier en Python :
# if len(sys.argv) > 1:
#     filename = sys.argv[1]
#     with open(filename, 'r') as file:
#         content = file.read()
#         print(content)

# Comment exécuter un autre programme :
# import sys
# import subprocess

# if len(sys.argv) > 1:
#     program_name = sys.argv[1]
#     subprocess.run([program_name])
