# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
pollpath = os.path.join("Resources", "election_data.csv")

totalvotes = 0
votes = {}

with open(pollpath) as pollfile:
    #This converts the file I opened into a dictionary
    pollreader = csv.DictReader(pollfile)
    for row in pollreader:
        # I use this method instead of taking the length of a list since I don't have a list the length of the data. That's it.
        totalvotes += 1
        if row["Candidate"] not in votes:
            votes.update({row["Candidate"] : 0})
        votes[row["Candidate"]] += 1

print(f'Total Votes: {totalvotes}')
for i in votes:
    percentage = int(votes[i]) / totalvotes
    percentage *= 100
    percentage = round(percentage, 0)
    print(f'{i}: {percentage}00% {votes[i]}')

highestvotes = max(votes.values())
winnername = None
for name, vote in votes.items():
    if vote == highestvotes:
        winnername = name
        print(f'Winner: {name}')

resultspath = os.path.join("Analysis", "pollresults.txt")

with open(resultspath, 'w') as results:
    results.write("Election Results\n")
    results.write("----------------\n")
    results.write(f'Total Votes: {totalvotes}\n')
    results.write("----------------\n")
    for i in votes:
        percentage = int(votes[i]) / totalvotes
        percentage *= 100
        percentage = round(percentage, 0)
        results.write(f'{i}: {percentage}00% {votes[i]}\n')
    results.write("----------------\n")
    results.write(f'Winner: {winnername}')