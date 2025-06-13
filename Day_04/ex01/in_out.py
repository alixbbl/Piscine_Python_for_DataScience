# Recoding some simple functions from the maths lib :


# fonction qui retourne le carré de l'argument
def square(x: int | float) -> int | float:
    return x * x


# fonction qui retourne l'argument puissance lui-même
def pow(x: int | float) -> int | float:
    return x**x


# fonction qui prend une fonction et un nbre en params, appel de la fonction interne
# à chaque appel de l'objet
def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count, x
        count += 1
        x = function(x)
        return x

    return inner
