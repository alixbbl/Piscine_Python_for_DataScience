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

	if not args:
		for function in kwargs:
			print("ERROR")
		return

	# On utilise ici des methodes à instances
	def mean(values):
		return sum(values) / len(values)

	def median(values):
		sorted_values = sorted(values)
		if (len(values) % 2):
			
