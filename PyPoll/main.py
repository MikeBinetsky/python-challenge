# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
pollpath = os.path.join("Resources", "election_data.csv")

totalvotes = 0
candidatelist = []

with open(pollpath) as pollfile:
    #This converts the file I opened into a dictionary
    pollreader = csv.DictReader(pollfile)
    for row in pollreader:
        totalvotes += 1
        if row["Candidate"] not in candidatelist:
            candidatelist.append(row["Candidate"])


print(f' Total Votes: {totalvotes}')
for i in candidatelist:
    print(i)