# PyPoll Challenge


# import modules
import csv
import os


# define what is being read and where to write results
input_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))


# create lists and variables
total_ballots = []
candidates = []

c1_votes = 0
c2_votes = 0
c3_votes = 0

c1 = 0
c2 = 0
c3 = 0


# read
with open(input_path, 'r') as csv_file_object:
    csvreader = csv.reader(csv_file_object, delimiter=",")
    next(csvreader) # skip header
    for row in csvreader:
        total_ballots.append(row[0])
        candidates.append(row[2])
for name in candidates:
    if name == "Charles Casper Stockham":
        c1_votes = c1_votes + 1
        c1 = c1 + 1
    if name == "Diana DeGette":
        c2_votes = c2_votes + 1
        c2 = c2 + 1
    if name == "Raymon Anthony Doane":
        c3_votes = c3_votes + 1
        c3 = c3 + 1

# calculate percentage of votes for each candidate
percent_c1 = c1_votes / len(total_ballots) * 100
percent_c1 = str(round(percent_c1, 3)) + "%"

percent_c2 = c2_votes / len(total_ballots) * 100
percent_c2 = str(round(percent_c2, 3)) + "%"

percent_c3 = c3_votes / len(total_ballots) * 100
percent_c3 = str(round(percent_c3, 3)) + "%"

# determine election winner
results = (max(c1, c2, c3))
if results == c1:
    winner = "Charles Casper Stockham"
elif results == c2:
    winner = "Diana DeGette"
elif results == c3:
    winner = "Raymon Anthony Doane"

# write
with open(output_path, 'w') as file_writer:
    file_writer.write(f"Election Results\n")
    file_writer.write(f"----------------------\n")
    file_writer.write(f"Total Votes: {len(total_ballots)}\n")
    file_writer.write(f"----------------------\n")
    file_writer.write(f"Charles Casper Stockham: {percent_c1} ({c1_votes})\n")
    file_writer.write(f"Diana DeGette: {percent_c2} ({c2_votes})\n")
    file_writer.write(f"Raymon Anthony Doane: {percent_c3} ({c3_votes})\n")
    file_writer.write(f"----------------------\n")
    file_writer.write(f"Winner: {winner}\n")
    file_writer.write(f"----------------------\n")

    print(f"Election Results\n")
    print(f"----------------------\n")
    print(f"Total Votes: {len(total_ballots)}\n")
    print(f"----------------------\n")
    print(f"Charles Casper Stockham: {percent_c1} ({c1_votes})\n")
    print(f"Diana DeGette: {percent_c2} ({c2_votes})\n")
    print(f"Raymon Anthony Doane: {percent_c3} ({c3_votes})\n")
    print(f"----------------------\n")
    print(f"Winner: {winner}\n")
    print(f"----------------------\n")