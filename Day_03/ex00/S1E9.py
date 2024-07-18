from abc import ABC, abstractmethod

# self est l' equivalent de this->, elle fait reference a l'instance de la classe.
class Character(ABC):
	"""
	This class takes a first_name as first mandatory parameter, is_alive as a
	non mandatory second set to True

	"""
	def __init__(self, first_name, is_alive=True):
		"""
		Constructor docstring : parent class constructor.
		"""
		self.first_name = first_name
		self.is_alive = is_alive
	@abstractmethod # decorateur qui implique que la methode est anstraite = comme virtuelle pure en c++
	def die(self): # pas de code ici, c'est aux classes qui heritent de mettre la methode
		pass

class Stark(Character):
	"""
	This class should inherit the Character class.
	"""
	def __init__(self, first_name, is_alive=True):
		"""
		Inheriting class Stark constructor.
		"""
		super().__init__(first_name, is_alive)
	def die(self):
		"""
		Method docstring : from alive to dead.
		"""
		self.is_alive = False

# super() est une fonction intégree qui permet d'acceder aux methodes de la classe
# parente d'une classe derivee.
