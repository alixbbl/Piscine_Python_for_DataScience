from S1E7 import Baratheon, Lannister

# En Python, on appelle héritage multiple le fait qu'une classe dérive de deux ou plusieurs classes parentes.
class King(Baratheon, Lannister):

	def __init__(self, first_name, is_alive=True):
		super().__init__(first_name, is_alive)
		# l'objet instancié va heriter d'abord des attribust et methods de la premiere classe dont sa classe derive.

	# methodes d'instance, pas de decorateur, prennent self en arg
	def set_eyes(self, new_eyes):
		self.eyes = new_eyes

	def set_hairs(self, new_hair):
		self.hairs = new_hair

	def get_eyes(self):
		return self.eyes

	def get_hairs(self):
		return self.hairs
