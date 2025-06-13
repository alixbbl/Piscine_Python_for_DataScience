import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_data(data):
    """
    This function creates a graph, the lines and manages the display of the various
    infos.
    """
    gdp_list = data["median_income_per_country_in_1900"].tolist()
    life_list = data["life_exp_per_country_1900"].tolist()
    plt.scatter(gdp_list, life_list)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    cash_to_show = ["300", "1k", "10k"]
    cash_values = [
        300,
        1000,
        10000,
    ]

    plt.xscale("log")
    cash_to_show = ["300", "1k", "10k"]
    cash_values = [300, 1000, 10000]
    plt.xticks(cash_values, cash_to_show)
    plt.show()


def main():

    life_exp_data = load("life_expectancy_years.csv")
    income_pp = load("income.csv")
    median_income_per_country_in_1900 = income_pp[["country", "1900"]]
    life_exp_per_country_1900 = life_exp_data[["country", "1900"]]
    median_income_per_country_in_1900.columns = [
        "country",
        "median_income_per_country_in_1900",
    ]
    life_exp_per_country_1900.columns = ["country", "life_exp_per_country_1900"]
    merged_data = pd.merge(
        median_income_per_country_in_1900, life_exp_per_country_1900, on="country")
    print(merged_data)
    plot_data(merged_data)


if __name__ == "__main__":
    main()
