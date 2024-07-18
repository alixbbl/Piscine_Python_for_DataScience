from setuptools import setup, find_packages

setup(
	name='ft_package',
	version='0.0.1',
	author='eagle',
	author_email='eagle@42.fr',
	description='A sample test package',
	url='https://github.com/eagle/ft_package', # `url` au lieu de `Homepage`
	license='MIT',  # Assurez-vous que la licence correspond à ce que vous voulez
	packages=find_packages(),
	classifiers=[
		'License :: OSI Approved :: MIT License',  # La licence sous laquelle est distribué votre package
		'Programming Language :: Python :: 3'  # Indique que le package est fait pour Python 3
	],
	entry_points={
		# Configuration des points d'entrée si nécessaire, ici vide
	},
	install_requires=[
		# Liste des dépendances nécessaires
	],
)

# Certains chanps de l'output du pip show -v ft_package, ne sont pas remplis dans le fichier
# setup.py mais sont générés par par la commandde pip une fois appelée.
# exemples : `Location`, `Requires`, `Required-by`, `Metadata-Version`, et `Installer`
# Les classifiers sont des metadonnes, sortes de "caracteristiques techniques" du package:
# classifiers=[
#         'Development Status :: 3 - Alpha',  # Peut être "3 - Alpha", "4 - Beta" ou "5 - Production/Stable" selon le stade de développement
#         'Intended Audience :: Developers',  # Indique à qui le package est destiné
#         'Topic :: Software Development :: Build Tools',
#         'License :: OSI Approved :: MIT License',  # La licence sous laquelle est distribué votre package
#         'Programming Language :: Python :: 3',  # Indique que le package est fait pour Python 3
#         'Programming Language :: Python :: 3.6',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#         'Programming Language :: Python :: 3.9',
#         'Operating System :: OS Independent',
# 		... # Indique que le package est indépendant du système d'exploitation
#     ],
