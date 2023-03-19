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


# import modules
import csv
import os


# define what is being read and where to write results
input_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# create lists
months = []
total = []
pl = []
pl_change = []


# read
with open(input_path, 'r') as csv_file_object:
    csvreader = csv.reader(csv_file_object, delimiter=",")
    next(csvreader) # skip header
    for row in csvreader:
        months.append(row[0])
        total.append(int(row[1]))
        pl.append(row[1])
for i in range(1, len(pl)):
    change = int(pl[i]) - int(pl[i - 1])
    pl_change.append(change)

avg_change = int(sum(pl_change))/int(len(pl_change))
avg_change = "$" + str(round(avg_change, 2))


    
 

# write
with open(output_path, 'w') as file_writer:
    file_writer.write("Financial Analysis\n")
    file_writer.write("--------------------\n")
    file_writer.write(f"Total months: {len(months)}\n")
    file_writer.write(f"Total: ${sum(total)}\n")
    file_writer.write(f"Average Change: {avg_change}\n")
    file_writer.write(f"Greatest Increase in Profits: \n")
    file_writer.write(f"Greatest Decrease in Profits: \n")
    print("Financial Analysis\n")
    print("--------------------\n")
    print(f"Total months: {len(months)}\n")
    print(f"Total: ${sum(total)}\n")
    print(f"Average Change: {avg_change}\n")
    print(f"Greatest Increase in Profits: \n")
    print(f"Greatest Decrease in Profits: \n")