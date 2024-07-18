# Arithmetics for a duo of vectors

class Calculator:

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		vector = [a * b for a, b in zip(V1, V2)]
		result = 0
		for element in vector:
			result = result + element #  ou result = sum(vector)
		print(f"Dot product is: {result}")

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		result = 0
		result = [float(a + b) for a, b in zip(V1, V2)]
		print(f"Add Vector is : {result}")

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		result = 0
		result = [float(a - b) for a, b in zip(V1, V2)]
		print(f"Sous Vector is : {result}")

# Les methodes d'instance prennent self en premier argument.
# Les méthodes de class prennent cls en argument et peuvent modifierla classe.
# Les méthodes static sont utilisables en dehors de la classe et ne
# prennent pas en arguments les attributs, ou self, ou cls.
