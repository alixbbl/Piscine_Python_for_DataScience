import sys
import matplotlib.pyplot as plt
from load_csv import load


def main():

    if len(sys.argv) != 2:
        print("AssertionError: too many arguments")
        sys.exit(1)
    if not sys.argv[1] == "Paris":
        print("File path must be a very parisian string")
        return None
    else:
        campus_target = "France"
    path = "life_expectancy_years.csv"
    data_all = load(path)
    campus_data = data_all[data_all["country"] == campus_target]
    if campus_data.empty:
        return None
    life_expectancy = campus_data.drop(columns=["country"])

    life_expectancy_list = life_expectancy.iloc[0, 1:].tolist()
    years_list = data_all.columns[1:].tolist()

    data_len = min(len(life_expectancy_list), len(years_list))
    if len(years_list) > data_len:
        years_list = years_list[:data_len]
    elif len(life_expectancy_list) > data_len:
        life_expectancy_list = life_expectancy_list[:data_len]

    plt.plot(years_list, life_expectancy_list)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    years_to_show = [1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080]
    ticks_locations = [
        years_list.index(str(year)) for year in years_to_show if str(year) in years_list
    ]
    ticks_labels = [str(year) for year in years_to_show if str(year) in years_list]
    plt.xticks(ticks_locations, ticks_labels)
    plt.show()


if __name__ == "__main__":
    main()
