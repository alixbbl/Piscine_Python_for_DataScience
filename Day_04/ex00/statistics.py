from typing import Any

# LES BUILTINS SONT INTERDITS

# import numpy as np
# Cet exercice peut se faire avec la lib NumPy. On nous demande ici
# de capturer tous les arguments passés à la fonction, de parser et
# ensuite de retourner des resultats (obtenus à partir de builtins de np).
# *args = arguments positionnels, on

# def ft_statistics(*args: Any, **kwargs: Any) -> None:

# 	if not args:
# 		for function in kwargs:
# 			print("ERROR")
# 		return

# 	arguments = np.array(args) # on met les arguments positionnels dans un array
# 	STATS_FUNCTIONS = {
# 		'mean' : lambda: np.mean(arguments),
# 		'median' : lambda: np.median(arguments),
# 		'quartile' : lambda: np.percentile(arguments, 25),
# 		'std' : lambda: np.std(arguments),
# 		'var' : lambda: np.var(arguments)
# 	}
# 	for stat_name, stat_function in kwargs.items():
# 		if not stat_function in STATS_FUNCTIONS:
# 			pass
# 		else:
# 			print(f"{stat_function} : {STATS_FUNCTIONS[stat_function]()}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Simple implementation of a statistic calculator.
    """
    if not args:
        for function in kwargs:
            print("ERROR")
        return None

    def mean(values):
        """
        Returns the mean of a container of values (list or tuple).
        """
        return sum(values) / len(values)

    def median(values):
        """
        Returns the median of a container of values (list or tuple).
        """
        sorted_values = sorted(values)
        middle_index = len(values) // 2
        if (len(values) % 2) == 1:
            return sorted_values[middle_index]
        else:
            return (sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2

    # cette fonction retourne des tuples
    def quartile(values):
        """
        Returns the quartiles of a container of values (list or tuple).
        """
        sorted_values = sorted(values)
        mid = (len(sorted_values) // 2)
        if len(sorted_values) % 2 == 0:
            lower_half = sorted_values[:mid]
            higher_half = sorted_values[mid:]
        else:
            lower_half = sorted_values[:mid]
            higher_half = sorted_values[mid + 1:]
        return median(lower_half), median(higher_half)

    def std_function(values):
        """
        Returns the standard deviation of a container of values (list or tuple).
        """
        mean_values = mean(values)
        variance = sum((x - mean_values) ** 2 for x in values) / len(values)
        std_val = variance**0.5
        return std_val

    def var_function(values):
        """
        Returns the variance of a container of values (list or tuple).
        """
        mean_values = mean(values)
        variance = sum((x - mean_values) ** 2 for x in values) / len(values)
        return variance

    STATS_FUNCTIONS = {
        "mean": lambda: mean(args),
        "median": lambda: median(args),
        "quartile": lambda: quartile(args),
        "std": lambda: std_function(args),
        "var": lambda: var_function(args),
    }

    for stat_name, stat_function in kwargs.items():
        if stat_function not in STATS_FUNCTIONS:
            pass
        else:
            print(f"{stat_function} : {STATS_FUNCTIONS[stat_function]()}")
