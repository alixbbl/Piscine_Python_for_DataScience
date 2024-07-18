from PIL import Image
import numpy as np

# Ici le but est de faire une fonction de filtres de couleurs, on passe donc
# un array RGB et on travaille ensuite dessus pour supprimer un pan de coloris.
# puis on transformera les tuples. Vise a nous familiariser avec les codes RGB
# ainsi que la syntaxe des tableaux multidimensionnels.

# autorisés : =, +, -, *
def ft_invert(array) -> np.ndarray:
	"""
	Inverts the color of the image received.

	Pas besoin de copier l'array, on enleve à 255 la valeur RGB, soit pile l'inverse.
	Il est possible de faire des calculs arithmetiques directement sur un array.
	"""
	array_invert = 255-array
	return array_invert

# autorisés : =, *
def ft_red(array) -> np.ndarray:
	"""
	Ici, on cherche à supprimer les canaux verts et bleus, on met donc ces deux valeurs
	à zéro, pour cela on copie (conserve la couleur R), puis on utilise la syntaxe
	[:, :, :] qui signifie "pour toutes les dimensions de l'image", on prend les valeurs Vert (1)
	et on les multiplie par zero pour les annuler.
	Cette syntaxe est utilisée dans le cadre des arrays multidimensionnels de la lib NumPy.
	"""
	array_red = array.copy()
	array_red[:, :, 1] = array_red[:, :, 1] * 0 #suppression du canal vert (numero 1)
	array_red[:, :, 2] = array_red[:, :, 2] * 0 #idem avec le bleu (numero 2)
	return array_red

# autorisés : =, -
def ft_green(array) -> np.ndarray:
	"""
	Même procédé mais avec le canal vert.
	"""
	array_green = array.copy()
	array_green[:, :, 0] = array_green[:, :, 0] - array_green[:, :, 0]
	array_green[:, :, 2] = array_green[:, :, 2] - array_green[:, :, 2]
	return array_green

# autorisés : =
def ft_blue(array) -> np.ndarray:
	"""
	Suppression des canaux rouges et verts.
	"""
	array_blue = array.copy()
	array_blue[:, :, 0] = 0  # met à zéro le canal rouge
	array_blue[:, :, 1] = 0  # met à zéro le canal vert
	return array_blue

# autorisés : =, /
def ft_grey(array) -> np.ndarray:
	"""
	On utilise convert(), pour cela il faut repasser par un format Image
	"""
	array_grey = array.copy()
	array_grey_img = Image.fromarray(array).convert("L")
	array_grey = np.array(array_grey_img)
	return array_grey

# Autre solution mais non demandées par la consigne :
# def ft_grey(array) -> np.ndarray:
# 	array_grey_img=Image.fromarray(array)
# 	array_grey=np.array(array_grey_img.convert("L"))
# 	return array_grey
