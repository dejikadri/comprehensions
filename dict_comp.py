"""
This program uses a dictionary comprehension to turn 2 lists of countries and captials
into a dictionary with countries as keys and the capitals as values
"""

list_country = ['Nigeria', 'Ghana', 'Cameroun', 'Togo', 'Egypt', 'Kenya']
list_capital = ['Abuja', 'Akra','Yaunde', 'Lome', 'Cairo', 'Nairobi']


def country_cap(country, capital):
    return {country[i]: capital[i] for i in range(len(country)) }
