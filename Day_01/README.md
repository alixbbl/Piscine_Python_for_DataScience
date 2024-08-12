# PYTHON : Day 01, les éléments à retenir

Le Day01 a pour objectif de pratiquer la lib NumPy, ou np.
Il s'agit de construire des arrays, sur lesquel on peut pratiquer diverses opérations.
On construit un array à partir d'une liste de la manière suivante :
`height_array = np.array(height)`
Pour inverser la conversion et revenir à une liste :
`list = array_list.tolist()`
=> On utilise souvent np.array(list) et list = array.tolist()

## Pour vérifier l'existence d'un path vers un fichier :
`if os.path.exists(path):`
Avec import os en entrée de code, on utilise la fonction exists() pour tester le path.

## Pour vérifier l'extension d'un fichier :
`_, extension = os.path.splitext(path)`
`		if extension.lower() in ['.jpeg', '.jpg']:`
la première ligne de ce code permet de scinder en deux le path, et de stocker dans la variable
extension, ce qui se situe après le point (point inclus).

## Utilisation des libs NumPy et PIL (Image module) :
Une image est en fait un array de code RGB, il est donc possible de jongler entre les deux formats.
`img_load = Image.fromarray(img_load_array)` ici on convertit en image, un array avec Image.fromarray().
`array_image = np.array(image)` pour faire l'inverse.
La fonction show() appliquée sur une image, va imprimer celle-ci à l'écran.
Attention, les images sont en 3 dimensions.
La fonction crop() permet de crop une image avec les dimensions soumises (4 args).
