import sys

import matplotlib.pyplot as plt
from load_csv import load


def filter_country_data_to_list(data, years_list, country):
    """
    This function filters the requested country data, then it shortens the list
    to the mandatory length of the graph.
    Returns a list of data (uses iloc and tolist()).
    """
    country_data = data[data["country"] == country]
    country_data = country_data[years_list]
    if not country_data.empty:
        return country_data.iloc[0].tolist()


def convert_population(data_list):
    """
    The .csv isn't written in plain int or floats but uses k and M abreviations.
    This function converts it into numbers. Returns a data list.
    """
    data_list_convert = data_list.copy()
    for i, value in enumerate(data_list_convert):
        if value.endswith("k"):
            data_list_convert[i] = float(value[:-1]) * 1000
        elif value.endswith("M"):
            data_list_convert[i] = float(value[:-1]) * 1000000
    print(f"Liste des populations converties est de : {data_list_convert}")
    return data_list_convert


def plot_data(years_list, french_data, country_name, country_data):
    """
    This function creates a graph, the lines and manages the display of the
    various infos.
    """
    plt.plot(years_list, french_data, label="France")
    plt.plot(years_list, country_data, label=country_name)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")

    years_to_show = [1800, 1840, 1880, 1920, 1960, 2000, 2040]
    ticks_locations = [
        years_list.index(str(year)) for year in years_to_show if str(year) in years_list
    ]
    ticks_labels = [str(year) for year in years_to_show if str(year) in years_list]
    plt.xticks(ticks_locations, ticks_labels)
    nb_to_show = [20000000, 40000000, 60000000]
    ticks_locations = nb_to_show
    ticks_labels = [f"{int(nb/1000000)}M" for nb in nb_to_show]
    plt.yticks(ticks_locations, ticks_labels)

    # Affichage
    plt.show()


def main():

    if len(sys.argv) != 2:
        print("AssertionError: too many arguments")
        sys.exit(1)

    data_all = load("population_total.csv")
    years_list = data_all.columns[1:].tolist()
    years_list = [year for year in years_list if "1800" <= year <= "2050"]
    french_data_list = filter_country_data_to_list(data_all, years_list, "France")
    selected_country = sys.argv[1]
    if not isinstance(selected_country, str):
        print("Argument must be a string")
        return None

    list_of_countries = data_all.iloc[1:, 0].tolist()
    found = False
    for country in list_of_countries:
        if country == selected_country:
            found = True
            break
    if not french_data_list or not found:
        print("Error: Requested country not found.")
        return None

    country_data_list = filter_country_data_to_list(
        data_all, years_list, selected_country
    )
    country_data_pop = convert_population(country_data_list)
    french_data_pop = convert_population(french_data_list)
    plot_data(years_list, french_data_pop, selected_country, country_data_pop)


if __name__ == "__main__":
    main()
