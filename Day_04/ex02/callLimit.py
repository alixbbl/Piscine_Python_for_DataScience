from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {repr(function)} call too many times")
        return limit_function
    return callLimiter

# c'est la fonction callLimiter() qui permet à callLimit() d'être appelée comme décorateur.
# Ici, on utilise nonlocal avec "count" mais pas avec "limit", c' est parce qu'en Python, meme
# une variable hors-scope peut être lue. Or ici limit est lue et non modifiée, seule count l'est, rendant
# nécessaire le recours à "nonlocal".
