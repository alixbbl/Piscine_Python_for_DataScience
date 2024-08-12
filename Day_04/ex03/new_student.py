from dataclasses import dataclass, field
import string, random

def generate_id() -> str:
	"""
	Function of the subject : generates an aleatory string of 15 cases.
	"""
	return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
	name: str
	surname: str
	login: str = field(init=False)
	active: bool = True
	id: str = field(default_factory=generate_id)

	def __post_init__(self):
		self.login = self.name[0] + self.surname
# on doit init login en deux temps car il n' est pas possible d' utiliser self directement dans la classe.
# l'instance n'étant pas encore defini, il est "trop tôt" pour utiliser self!
# Il faut donc utiliser __post_init__(self).
