# ************* PYTHON PISCINE - DAY 0 *************

# ******************* Exercice 6a *******************

"""
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

import sys

# si la fonction n'existe pas, on retourne les items qui sont True
# cette fonction va retourner une "liste par compréhension"
def ft_filter(function, seq):
	if function is None:
		return[item for item in seq if item]
	else:
		return [item for item in seq if function(item)]

def main():
	# Comparer avec le comportement classique de la fonction si les args sont pas bons
	if len(sys.argv) != 3:
		sys.exit(1)

	function = sys.argv[1]
	if function.lower() == 'none': # on teste avec lower pour eviter les erreurs de casse
		function = None # si la fonction est bien 'none', on la remplace par None
	else:
		try:
			function = eval(function) # on teste la fonction pour voir si elle peut exister en Python, si son expression est valide
		except Exception as e:
			print(e)
			sys.exit(1)

	try:
		seq = sys.argv[2].split(',')
	except Exception as e:
		print(e)
		sys.exit(1)

	result = ft_filter(function, seq)
	print(result)

if __name__ == "__main__":
	main()


# Comment recuperer et ouvrir un fichier en Python :
# if len(sys.argv) > 1:
#     filename = sys.argv[1]
#     with open(filename, 'r') as file:
#         content = file.read()
#         print(content)

# Comment exécuter un autre programme :
# import sys
# import subprocess

# if len(sys.argv) > 1:
#     program_name = sys.argv[1]
#     subprocess.run([program_name])
