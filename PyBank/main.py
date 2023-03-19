# PyBank Challenge:


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
pl_date = []

# read
with open(input_path, 'r') as csv_file_object:
    csvreader = csv.reader(csv_file_object, delimiter=",")
    next(csvreader) # skip header
    for row in csvreader:
        months.append(row[0])
        total.append(int(row[1]))
        pl.append(row[1])
        pl_date.append(row[0])
for i in range(1, len(pl)):
    change = int(pl[i]) - int(pl[i - 1])
    pl_change.append(change)


for value in range(len(pl_change)):
    if pl_change[value] == max(pl_change):
        pl_date_max = (pl_date[value + 1])
    if pl_change[value] == min(pl_change):
        pl_date_min = (pl_date[value + 1])


avg_change = int(sum(pl_change))/int(len(pl_change))
avg_change = "$" + str(round(avg_change, 2))
 

# write
with open(output_path, 'w') as file_writer:
    file_writer.write("Financial Analysis\n")
    file_writer.write("--------------------\n")
    file_writer.write(f"Total Months: {len(months)}\n")
    file_writer.write(f"Total: ${sum(total)}\n")
    file_writer.write(f"Average Change: {avg_change}\n")
    file_writer.write(f"Greatest Increase in Profits: {pl_date_max} ${max(pl_change)}\n")
    file_writer.write(f"Greatest Decrease in Profits: {pl_date_min} ${min(pl_change)}\n")
    print("Financial Analysis\n")
    print("--------------------\n")
    print(f"Total Months: {len(months)}\n")
    print(f"Total: ${sum(total)}\n")
    print(f"Average Change: {avg_change}\n")
    print(f"Greatest Increase in Profits: {pl_date_max} ${max(pl_change)}\n")
    print(f"Greatest Decrease in Profits: {pl_date_min} ${min(pl_change)}\n")