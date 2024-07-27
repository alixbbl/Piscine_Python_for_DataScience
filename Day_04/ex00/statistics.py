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
		return None

	# On utilise ici des methodes à instances
	def mean(values):
		return sum(values) / len(values)

	def median(values):
		sorted_values = sorted(values)
		middle_index = len(values) // 2
		if (len(values) % 2) == 1:
			return sorted_values[middle_index]
		else: # si on a un nbre pair, la mediane est la moyenne des deux index du milieu
			return (sorted_values[middle_index - 1] + sorted_values[middle_index]) / 2

	# cette fonction retourne des tuples 
	def quartile(values):
		sorted_values = sorted(values)
		mid = len(sorted_values) // 2 # on recherche un index, si nbr pair, le mid est la valeur juste apres le milieu
		if (len(sorted_values) % 2 == 0): # si on a un nbre pair de valeurs
			lower_half = sorted_values[:mid] # on tronque la liste de valeurs a partir de mid(milieu)
			higher_half = sorted_values[mid:]
		else:
			lower_half = sorted_values[:mid]
			higher_half = sorted_values[mid + 1:]
		return median(lower_half), median(higher_half)
	
	# std est une fonction qui retourne l'écart type d'un ensemble de données
	# l'écart type est une mesure de dispersion des valeurs par rapport á la moyenne
	# plus il est élevé, plus les valeurs de l'ensemble s'éloigne de la moyenne
	# on calcule pour l'obtenir, la variance : moyenne des carrés des écarts à la moyenne
	# l'écart type est la racine carrée de la variance
	def std_function(values):
		mean_values = mean(values) 
		variance = sum((x - mean_values) ** 2 for x in values) / len(values)
		std_val = variance ** 0.5
		return std_val
	
	# mesure de la dispersion des valeurs autour de la valeur moyenne
	# la diff avec l'écart type est leur unité d'expression! une variance est en metres carrés
	# c'est donc une valeur plus difficilement interpretable que l'ecart type (meme unité que les valeurs de l'ensemble)
	def var_function(values):
		mean_values = mean(values) 
		variance = sum((x - mean_values) ** 2 for x in values) / len(values)
		return variance
	
	STATS_FUNCTIONS = {
		'mean' : lambda: mean(args),
		'median' : lambda: median(args),
		'quartile' : lambda: quartile(args),
		'std' : lambda: std_function(args),
		'var' : lambda: var_function(args)
	}
	
	for stat_name, stat_function in kwargs.items():
		if not stat_function in STATS_FUNCTIONS:
			pass
		else:
			print(f"{stat_function} : {STATS_FUNCTIONS[stat_function]()}")