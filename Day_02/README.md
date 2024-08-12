# DAY 02 : DATASET ET DATATABLES

## PANDAS LIB ET MANIPULATION DES DATASET ET DATATABLES

Pandas est une bibliothèque logicielle écrite pour le langage de programmation Python pour la manipulation et l'analyse de données. Voici les informations générales sur les composants clés de Pandas : les DataFrame et les Series.

**DataFrame**
Un DataFrame est une structure de données bidimensionnelle, essentiellement une table avec des lignes et des colonnes.
Chaque colonne dans un DataFrame peut avoir un type différent (numérique, chaîne, booléen, etc.).
Les DataFrames sont idéaux pour représenter des données réelles : des feuilles de calcul Excel, des tables SQL, etc.
Faire appel a la fonction load() via un path, permet de retourner un dataset.

**Series**
Une Series est une structure de données unidimensionnelle. On peut la considérer comme une colonne d'un DataFrame.
Tous les éléments d'une Series doivent être du même type de données.
Les Series sont utiles pour représenter des séries temporelles, des séquences de valeurs, etc.

## Utilisation de Pandas
Pour utiliser Pandas, il faut d'abord l'importer. Voici comment faire :
`import pandas as pd`

**Création d'un DataFrame**
Voici un exemple simple de création d'un DataFrame :

`data = {'Nom': ['Jean', 'Marie', 'Pierre'],`
`        'Age': [23, 34, 45],`
`        'Ville': ['Paris', 'Lyon', 'Marseille']}`
`df = pd.DataFrame(data)`

**Création d'une Series**
Voici comment créer une Series :
`s = pd.Series([1, 3, 5, 7, 9])`

**Manipulation de données**
Pandas offre une large gamme de fonctions pour nettoyer, transformer, manipuler et analyser les données. Quelques opérations courantes incluent :

	- Filtrage et sélection de données
	- Fusion et jointure de DataFrames
	- Gestion des données manquantes
	- Groupement et agrégation de données
	- Tri et réorganisation

Pandas est extrêmement puissant pour traiter et analyser des données tabulaires et est largement utilisé dans les domaines de la science des données, de l'analyse statistique, et de l'ingénierie logicielle pour des tâches liées aux données.

**Deux méthodes incontournables:**
Les méthodes de DataFrame iloc et loc permettent de récupérer de la data dans un DataFrame, soit
à partir du label, soit a partir de l'index:
	*loc*
		Utilisation : Accède aux lignes et colonnes par leurs labels.
		- Syntaxe : df.loc[<row_labels>, <column_labels>]
		- Exemples :
			Sélectionner toutes les lignes pour une colonne spécifique : df.loc[:, 'column_name']
			Sélectionner une ligne spécifique pour toutes les colonnes : df.loc['row_label', :]
			Sélectionner des lignes et colonnes spécifiques : df.loc[['row_label1', 'row_label2'], ['column_name1', 'column_name2']]
	*iloc*
	Utilisation : Accède aux lignes et colonnes par leurs positions numériques (indices).
	- Syntaxe : df.iloc[<row_positions>, <column_positions>]
	- Exemples :
		Sélectionner toutes les lignes pour une colonne spécifique par son indice : df.iloc[:, 0] (pour la première colonne)
		Sélectionner une ligne spécifique pour toutes les colonnes par son indice : df.iloc[0, :] (pour la première ligne)
		Sélectionner des lignes et colonnes spécifiques par leurs indices : df.iloc[[0, 1], [0, 1]] (pour les deux premières lignes et colonnes)


## MATPLOTLIB : Utilisation graphique

Matplotlib est une bibliothèque de visualisation de données en Python qui permet de créer des graphiques statiques, animés et interactifs. Elle est conçue pour fonctionner avec des tableaux NumPy et Pandas, ce qui la rend extrêmement utile pour la science des données et l'analyse de données. Voici quelques points clés sur Matplotlib :

**Fonctionnalités**

	- Graphiques 2D et 3D : Matplotlib peut créer une grande variété de graphiques, y compris des histogrammes, des graphiques à barres, des graphiques linéaires, des diagrammes de dispersion, des graphiques en camembert, etc.
	- Personnalisation : Les graphiques générés peuvent être largement personnalisés en termes de styles, de polices, de couleurs et de mises en page pour répondre aux besoins spécifiques de présentation.
	- Intégration : Elle s'intègre bien avec les environnements de notebook Jupyter pour afficher les graphiques directement dans les notebooks.
	- Exportation : Les graphiques peuvent être exportés dans de nombreux formats de fichiers raster et vectoriels, tels que PNG, PDF, SVG, etc.

**Utilisation de base**

Pour utiliser Matplotlib, vous devez d'abord l'importer, généralement avec Pyplot, qui est une interface permettant de créer des figures et des graphiques.
Voici un exemple simple :

`import matplotlib.pyplot as plt`

`# Données`
`x = [1, 2, 3, 4]`
`y = [10, 20, 25, 30]`

`# Créer un graphique`
`plt.plot(x, y)`

`# Titre et étiquettes`
`plt.title("Exemple simple")`
`plt.xlabel("Axe X")`
`plt.ylabel("Axe Y")`

`# Afficher le graphique`
`plt.show()``

*Pourquoi utiliser Matplotlib ?*

	- Flexibilité : Capable de créer une grande variété de graphiques et de visualisations.
	- Popularité : L'une des bibliothèques de visualisation les plus utilisées en Python, avec une grande communauté et beaucoup de ressources d'apprentissage.
	- Compatibilité : Fonctionne bien avec d'autres bibliothèques de science des données en Python, comme NumPy et Pandas.

Matplotlib est un outil essentiel pour l'analyse de données et la science des données, permettant aux utilisateurs de visualiser les données de manière significative et de communiquer les résultats de manière visuelle.
