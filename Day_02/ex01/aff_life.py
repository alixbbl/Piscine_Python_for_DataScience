from load_csv import load
import matplotlib.pyplot as plt
import sys

# Objectif :
# Créer un programme.
# Ce programme va devoir :
# - Faire appel à load(), cette fonction retourne un dataset.
# - Sélectionner les infos du campus souhaité (ici Paris).
# - Afficher les infos du campus de Paris.
# - Avoir en plus une légende et des axes nommés.

def main():

	if (len(sys.argv) != 2):
		print("AssertionError: too many arguments")
		sys.exit(1)
	if not sys.argv[1] == "Paris":
		print("File path must be a very parisian string")
		return None
	else:
		campus_target = "France"
	path = "life_expectancy_years.csv"
	data_all = load(path)
	# print(data_all.info())
	# On va chercher les infos dans le set, comme en C++ (clef/valeur)
	campus_data = data_all[data_all['country'] == campus_target]
	if campus_data.empty:
		return None

	# La ligne suivante supprime la column country "France" pour ne garder
	# que les infos de la life_expectancy de la France => nouveau dataset créé.
	life_expectancy = campus_data.drop(columns=['country'])

	# Les deux datasets obtenus ne sont pas facilement manipulables en tant que suite
	# de nombres, et ce sont des objets bidimensionnels, on les convertit
	# donc en listes pour aller vers la production du graphique.
	life_expectancy_list = life_expectancy.iloc[0, 1:].tolist()
	years_list = data_all.columns[1:].tolist()

	# On ajuste le nombre de colonnes car les deux axes x, y doivent être de mm longueurs
	data_len = min(len(life_expectancy_list), len(years_list))
	if len(years_list) > data_len:
		years_list = years_list[:data_len]
	elif len(life_expectancy_list) > data_len:
		life_expectancy_list = life_expectancy_list[:data_len]

	# On crée le graphique avec MatPlotLib :
	plt.plot(years_list, life_expectancy_list)
	plt.title("France Life expectancy Projections")
	plt.xlabel("Year")
	plt.ylabel("Life expectancy")

	# Modifier l'affichage par défaut des annees en abscisse :
	years_to_show = [1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080]
	ticks_locations = [years_list.index(str(year)) for year in years_to_show if str(year) in years_list]
	ticks_labels = [str(year) for year in years_to_show if str(year) in years_list]

	# Appliquer les ticks personnalisés sur l'axe des x
	plt.xticks(ticks_locations, ticks_labels)

	# Affichage
	plt.show()

if __name__ == "__main__":
	main()
