# PyBank Challenge:

# Create a Python script that analyzes the records (budget_data.csv) to calculate
# each of the following values:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period
# Your final script should both print the analysis to the terminal and export a 
# text file with the results

import csv
import os


INPUT_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "results.txt")


os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())

# csv_file_object = open(INPUT_PATH)
# print(csv_file_object.read())
# csv_file_object.close()

with open(INPUT_PATH) as csv_file_object:
    print(csv_file_object.read())

results = (
    "TBD\n"
    "Done\n"
)

with open(OUTPUT_PATH, 'w') as output_file_object:
    print(results)
    output_file_object.write(results)
