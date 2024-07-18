from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_data(data):

	"""
	This function creates a graph, the lines and manages the display of the various infos.
	"""
	gdp_list = data['median_income_per_country_in_1900'].tolist()
	life_list = data['life_exp_per_country_1900'].tolist()
	plt.scatter(gdp_list, life_list) # Pas une courbe mais un nuage de points
	plt.title("1900")
	plt.xlabel("Gross domestic product")
	plt.ylabel("Life expectancy")

	# Modifier l'affichage par défaut des annees en abscisse :
	cash_to_show = ['300', '1k', '10k']
	cash_values = [300, 1000, 10000]  # Corrected the third value to match the label '10k'

	# Calculate tick locations based on the range of gdp_list
	plt.xscale('log') # echelle logarithmique pour rendre le nuage plus compréhensible
	# personnalisation des etiquettes :
	cash_to_show = ['300', '1k', '10k']
	cash_values = [300, 1000, 10000]
	# xticks comme yticks prennent deux arguments (valeurs, etiquettes des valeurs)
	plt.xticks(cash_values, cash_to_show)

	# Affichage
	plt.show()

def main():

	life_exp_data = load("life_expectancy_years.csv")
	income_pp = load("income.csv")

	# On ne peut pas filtrer income.csv comme avec 'country' car pas de classe 'year'
	# Donc on va prendre et créer un nouveau dataframe à partir du dataframe global loaded
	median_income_per_country_in_1900 = income_pp[['country', '1900']]

	# Sélectionner la life_exp en 1900 pour chaque pays:
	life_exp_per_country_1900 = life_exp_data[['country', '1900']]

	# On va fusionner les deux dataframe sur la colonne country, auparavant on renomme 1900
	# Pour fusionner les deux DF, on utilise la fonction merge()
	median_income_per_country_in_1900.columns = ['country', 'median_income_per_country_in_1900']
	life_exp_per_country_1900.columns = ['country', 'life_exp_per_country_1900']
	merged_data = pd.merge(median_income_per_country_in_1900, life_exp_per_country_1900, on='country')

	print(merged_data)
	plot_data(merged_data)

if __name__ == "__main__":
	main()
