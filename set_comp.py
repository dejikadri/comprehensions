import csv
import os

"""
This program uses list comprehension and sets to parse a csv file of 100,000 sales records
and and 14 columns to extract the country(second column) and output unique country names

"""


def set_comp_countries(csv_file):
    file_o = open(csv_file)

    st_country = {country[1] for country in csv.reader(file_o)}
    file_o.close()
    return sorted(st_country)

#print(set_comp_countries('100000_Sales_Records.csv'))

# '''
# This program uses list comprehension to list particular file extension in a directory
#
# '''
# x = [f for f in os.listdir('.')
#             if f.endswith('csv')]
# print x




