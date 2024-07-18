# On s'inspire ici de slice_me mais en utilisant des fonctions des lib (Pillow pour les images, numpy
# pour les arrays).

from load_image import ft_load
from PIL import Image
import numpy as np

def zoom_image(path_img, start_row, end_row, start_col, end_col):
	"""
	Load an image, slice it to the specified region, and convert that region to grayscale.

	:param path_img: Path to the image file.
	:param start_row: Start index for rows.
	:param end_row: End index for rows.
	:param start_col: Start index for columns.
	:param end_col: End index for columns.
	:return: A NumPy array of the sliced and grayscaled region.
	"""
	# Ici on emploie la fonction ft_load, elle retourne un ArrayNP, à convertir
	img_load_array = ft_load(path_img)
	print(img_load_array)
	# Puis on convertit cet array de RGB grâce a la fonction suivante :
	img_load = Image.fromarray(img_load_array)
	# On peut ensuite utiliser les methodes des objets Image comme crop() et convert()
	image_zoomed = img_load.crop((start_col, start_row, end_col, end_row))
	image_gray_zoomed = image_zoomed.convert("L")

	# Convert the PIL image to a NumPy array
	np_image = np.array(image_gray_zoomed)

	# On ajoute une 3e dimension comme demandé par la consigne (400, 400, 1), ajoute le 1.
	np_image_reshaped = np.expand_dims(np_image, axis=-1)

	print(f"New shape after slicing: {np_image_reshaped.shape} or ({end_row - start_row}, {end_col - start_col})")
	print(np_image_reshaped)
	return np_image_reshaped

def main():
	new_image = zoom_image("animal.jpeg", 100, 500, 100, 500)
	# si on travaille avec un fichier PIL image, on peut l'afficher avec show() à l'ecran!
	# ici, new_image issue de zoom_image est encore un array, on doit donc le reconvertir pour
	# utiliser show().
	Image.fromarray(new_image[:,:,0]).show()

if __name__ == "__main__":
	main()
