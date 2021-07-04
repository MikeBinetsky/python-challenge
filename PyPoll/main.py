# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
pollpath = os.path.join("Resources", "election_data.csv")

totalvotes = 0
candidatelist = []
votes = {}

with open(pollpath) as pollfile:
    #This converts the file I opened into a dictionary
    pollreader = csv.DictReader(pollfile)
    for row in pollreader:
        # I use this method instead of taking the length of a list since I don't have a list the length of the data. That's it.
        totalvotes += 1
        if row["Candidate"] not in candidatelist:
            candidatelist.append(row["Candidate"])
            votes.update({row["Candidate"] : 0})
        votes[row["Candidate"]] += 1

print(f'Total Votes: {totalvotes}')
for i in candidatelist:
    print(f'{i}: {votes[i]}')