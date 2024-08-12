# Arithmetics for a duo of vectors

class Calculator:
	"""
	This class uses static method to operate as a simple arithmetic calculator.
	"""
	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		"""
		This static takes two vectors and returns the dotproduct of it. Dotproduct is the sum of v1xv2.
		Prints the result on screen. Result is a single number.
		"""
		vector = [a * b for a, b in zip(V1, V2)]
		result = 0
		for element in vector:
			result = result + element #  ou result = sum(vector)
		print(f"Dot product is: {result}")

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		"""
		This static takes two vectors and returns the vectoriel product of it.
		Prints the result on screen. Result is a vector.
		"""
		result = 0
		result = [float(a + b) for a, b in zip(V1, V2)]
		print(f"Add Vector is : {result}")

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		"""
		This static takes two vectors and returns the vectoriel difference of it.
		Prints the result on screen. Result is a vector.
		"""
		result = 0
		result = [float(a - b) for a, b in zip(V1, V2)]
		print(f"Sous Vector is : {result}")

# Les methodes d'instance prennent self en premier argument.
# Les méthodes de class prennent cls en argument et peuvent modifierla classe.
# Les méthodes static sont utilisables en dehors de la classe et ne
# prennent pas en arguments les attributs, ou self, ou cls.
