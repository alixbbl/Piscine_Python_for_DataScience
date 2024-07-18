import numpy as np

# Methode sans utiliser numpy
# def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

# 	bmi = []
# 	for h, w in zip(height, weight):
# 		bmi_value = w / (h ** 2)
# 		bmi.append(bmi_value)
# 	return bmi


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

# 	limits=[]
# 	for element in bmi:
# 		if element > limit:
# 			limits.append(False)
# 		else:
# 			limits.append(True)
# 	return(limits)

# Pour une fonction qui prend deux listes, en faisant des operations sur les paires
# de ces listes, on peut utiliser l'outil zip, qui associe deux elements!

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
	This function is meant to convert list arguments in arrays, using np module from
	the numpy lib. Then, operations can be perform on the newly created arrays.
	"""
	height_array = np.array(height)
	weight_array = np.array(weight)

	for h in height_array:
		if not (isinstance(h, int) or isinstance(h, float)):
			print("AssertionError: arguments are bad")
			exit(1)
	for w in weight_array:
		if not (isinstance(w, int) or isinstance(w, float)):
			print("AssertionError: arguments are bad")
			exit(1)
	if len(weight_array) != len(height_array):
		print("AssertionError: lists are not same size")
		exit(1)
	bmi = weight_array / height_array**2
	return bmi.tolist()
# ici on prend une liste et on la cnvertit en objet np de type array
# on peut ensuite faire des operations sur les deux arrays créés

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	This function is meant to compare all the elements of the array,
	be cautious with the use of different types (lists nd arrays),
	some conversions are required.
	"""
	bmi_array = np.array(bmi)
	limits = bmi_array > limit
	return limits.tolist()
