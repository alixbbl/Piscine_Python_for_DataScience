# Attention : pas de lib autorisée pour transpose.
# Rappel : ft_load retourne un Numpy Array.

from load_image import ft_load
from PIL import Image
import numpy as np
import math

# permet de faire pivoter un array de type NumPy
def ft_rotate(img_array, angle):
	height, width = img_array.shape[:2] # shape retourne un tuple contenant les dimensions, on garde les deux principales
	new_img_array = np.zeros_like(img_array) # on cree un array vide pour y stocker la new img, de memes dimensions

	angle_rad = math.radians(angle)
	c_x, c_y = width /2, height / 2

	for y in range(height):
			for x in range(width):
				# Calcul des nouvelles positions
				new_x = int((x - c_x) * math.cos(angle_rad) - (y - c_y) * math.sin(angle_rad) + c_x)
				new_y = int((x - c_x) * math.sin(angle_rad) + (y - c_y) * math.cos(angle_rad) + c_y)

				# Vérification que les nouvelles positions sont dans les limites de l'image
				if 0 <= new_x < width and 0 <= new_y < height:
					new_img_array[new_y, new_x] = img_array[y, x]
	return new_img_array

def ft_transpose(path_img, start_row, end_row, start_col, end_col, angle):
	"""
	Load an image, cut it into a square and rotate it before printing it in grayscale.

	:param path_img: Path to the image file.
	:param start_row: Start index for rows.
	:param end_row: End index for rows.
	:param start_col: Start index for columns.
	:param end_col: End index for columns.
	:param angle : Rotation angle.
	:return: A NumPy array of the sliced and grayscaled region.
	"""
	img_load_array = ft_load(path_img)
	img_load = Image.fromarray(img_load_array)
	img_cut = img_load.crop((start_col, start_row, end_col, end_row)) # attention au tuple pour crop()
	img_gray_cut = img_cut.convert("L")
	img_gray_cut_array = np.array(img_gray_cut)
	gray_cut_array_reshaped = np.expand_dims(img_gray_cut_array, axis=-1) # premier ajout de la 3e dimension

	print(f"The shape of image is: {gray_cut_array_reshaped.shape} or ({end_row - start_row}, {end_col - start_col})")
	print(gray_cut_array_reshaped)
	# On est ici au niveau de l'exercice précédent, il faut maintenant faire la rotation de l'image

	# Rotation :
	rotated_img = ft_rotate(gray_cut_array_reshaped, 90)
	print(f"New shape after Transpose: {rotated_img.shape[:2]}")
	print(rotated_img)
	return rotated_img
	# Il faut a nouveau ajouter la 3dim car la rotation se fait sur un 2D array, la 3d est perdue
	# il s'agit avant tout d'un souci de compatibilite pour les affichages des images

def main():
	rotated_image = ft_transpose("animal.jpeg", 100, 500, 100, 500, 90)
	# Idem, on doit convertir le return de l'array en PIL image, si
	Image.fromarray(rotated_image[:,:,0]).show()

if __name__ == "__main__":
	main()
