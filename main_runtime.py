import pandas as pd
import matplotlib.pyplot as plt

"""
The start of the script is where we read in the data and create a set of countries that were in both 1990 and 2020.

"""

renewables_df = pd.read_csv('renewable-share-energy.csv')
co2_df = pd.read_csv('consumption-co2-per-capita.csv')

renewables_1990 = renewables_df[renewables_df['Year'] == 1990]['Entity']
co2_1990 = co2_df[co2_df['Year'] == 1990]['Entity']

renewables_2020 = renewables_df[renewables_df['Year'] == 2020]['Entity']
co2_2020 = co2_df[co2_df['Year'] == 2020]['Entity']

countries_1990 = set(renewables_1990).intersection(co2_1990)
countries_2020 = set(renewables_2020).intersection(co2_2020)

countries_both_years = countries_1990.intersection(countries_2020)

non_country_entities = [
    'High-income countries', 'South America', 'Europe', 'Oceania', 'Africa',
    'Lower-middle-income countries', 'Upper-middle-income countries', 'World',
    'North America', 'European Union (27)', 'Asia'
]

filtered_countries = set(countries_both_years) - set(non_country_entities)

sorted_filtered_countries = sorted(filtered_countries)

# Filter datasets to only include the countries in 'sorted_filtered_countries'
filtered_renewables_df = renewables_df[renewables_df['Entity'].isin(sorted_filtered_countries)]
filtered_co2_df = co2_df[co2_df['Entity'].isin(sorted_filtered_countries)]

# Filter the 'renewables_df' for years 1990 to 2020
renewables_df_1990_2020 = filtered_renewables_df[(filtered_renewables_df['Year'] >= 1990) & (filtered_renewables_df['Year'] <= 2020)]
average_renewables_by_year = renewables_df_1990_2020.groupby('Year')['Renewables (% equivalent primary energy)'].mean().tolist()

# Filter the 'co2_df' for years 1990 to 2020
co2_df_1990_2020 = filtered_co2_df[(filtered_co2_df['Year'] >= 1990) & (filtered_co2_df['Year'] <= 2020)]
average_co2_by_year = co2_df_1990_2020.groupby('Year')['Per capita consumption-based CO₂ emissions'].mean().tolist()


