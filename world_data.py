# world_data.py
# AUTHOR NAME: Melissa Liao
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 5 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library, including numpy and pandas.
# Remember to include docstrings and comments.

import numpy as np
import pandas as pd
from pandas.core import indexing

# Required function
def find_null(data, sub_reg):
    """ Function finds any null values in the 'Sq Km' column within the UN Sub-Region chosen by the user.

        Parameters:
            data: user should input the dataframe that wants to analyze. In this case, 
                  we would put in the data (world_data) provided for this particular assignment.
            sub_reg: represents the UN Sub-Region chosen by the user.
        
        Returns:
            If any null values are found, it will print out the UN Region, UN Sub-Region, the countries
            and its null values for Sq Km. If no null values are found, it will provide a message
            indicating no missing sq km values are found in the chosen UN Sub-Region.
    """
    subreg_sqkm_data = data.loc[pd.IndexSlice[:, sub_reg, :], pd.IndexSlice['Sq Km']]
    if subreg_sqkm_data.isnull().values.any() == True:
        print("\nSq km measurements are missing for:")
        print(subreg_sqkm_data[subreg_sqkm_data.isnull()])
    else:
        print("\nThere are no missing sq km values for this sub-region.")


def main():

    # Stage 1: Import data
    world_data = pd.read_excel(r".\Assign5Data.xlsx", index_col = [1, 2, 0]).sort_index()

    print("ENSF 592 World Data")

    # Stage 2: Request user input
    while True:
    # User must input correct Sub-Region name that is in the list of UN Sub-Region level.
    # Otherwise, it will prompt user with a ValueError message until a correct Sub-Region is input.
        try:
            chosen_subreg = input("Please enter a sub-region: ")
            if  chosen_subreg not in set(world_data.index.get_level_values('UN Sub-Region')):
                raise ValueError()
            break
        except ValueError:
            print("You must enter a valid UN sub-region name")
            

    # Stage 3: Find any missing sq km data values for the chosen sub-region
    find_null(world_data, chosen_subreg)

    # Stage 4: Calculations and dataset printing for the chosen sub-region
    # Adds two more columns in dataframe: Delta Population and Density
    print("\nCalculating change in population and latest density...\n")   
    world_data['Delta Population'] = world_data['2020 Pop'] - world_data['2000 Pop']
    world_data['Density'] = world_data['2020 Pop'] / world_data['Sq Km']
    print(world_data.loc[pd.IndexSlice[:, chosen_subreg, :], :])

    # Views a sub-array in the number of threatened species type per country of chosen sub-region
    print("\nNumber of threatened species in each country of the sub-region:\n")
    threat_species = world_data.loc[pd.IndexSlice[:, chosen_subreg, :], pd.IndexSlice['Plants (T)':'Mammals (T)']]
    print(threat_species)

    # Calculates the sq km area per the total number of threatened species for each country of chosen sub-region
    print("\nThe calculated sq km area per number of threatened species in each country is:\n")
    world_data['Sq Km per Threatened Species'] = world_data['Sq Km'] / np.sum(threat_species, axis=1)
    print(world_data.loc[pd.IndexSlice[:, chosen_subreg, :], pd.IndexSlice['Sq Km per Threatened Species']])

    # project_data.to_excel(r"./Assign5DataExport.xlsx", index = True, header = True)

if __name__ == '__main__':
    main()

