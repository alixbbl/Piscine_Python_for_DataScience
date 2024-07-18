# Arithmetics on a single vector

class Calculator():

	def __init__(self, vector):
		self.v = vector # on stocke le tuple dans l'attribut, en fait, Calculator est un vecteur

	def __add__(self, other) -> None:
		if isinstance(other, Calculator): # si l'other est de la meme nature que Calculator (un vecteur)
			if len(self.v) != len(other.v):
				raise ValueError("Compared others(tuples) are not the same size.")
			result = [a + b for a, b in zip(self.v, other.v)]
		else:
			result = [a + other for a in self.v]
		print(result)

	def __mul__(self, other) -> None:
		if isinstance(other, Calculator):
			if len(self.v) != len(other.v):
				raise ValueError("Compared others(tuples) are not the same size.")
			result = [a * b for a, b in zip(self.v, other.v)]
		else:
			result = [a * other for a in self.v]
		print(result)

	def __sub__(self, other) -> None:
		if isinstance(other, Calculator):
			if len(self.v) != len(other.v):
				raise ValueError("Compared others(tuples) are not the same size.")
			result = [a - b for a, b in zip(self.v, other.v)]
		else:
			result = [a - other for a in self.v]
		print(result)

	def __truediv__(self, other) -> None:
		if isinstance(other, Calculator):
			if len(self.v) != len(other.v):
				raise ValueError("Compared others(tuples) are not the same size.")
			for element in other.v:
				if element == 0:
					raise ValueError("Division by zero is forbidden.")
			result = [a / b for a, b in zip(self.v, other.v)]
		else:
			if other == 0:
				raise ValueError("Division by zero is forbidden.")
			else:
				result = [a / other for a in self.v]
		print(result)
