# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
pollpath = os.path.join("Resources", "election_data.csv")

totalvotes = 0
votes = {}

with open(pollpath) as pollfile:
    # This converts the file I opened into a dictionary
    pollreader = csv.DictReader(pollfile)
    for row in pollreader:
        # I use this method instead of taking the length of a list since I don't have a list the length of the data. That's it.
        totalvotes += 1
        # This if statement checks if the current row's candidate is in our votes dictionary. 
        # If they aren't, they are added to the dictionary with a starting vote of zero.
        if row["Candidate"] not in votes:
            votes.update({row["Candidate"] : 0})
        # Then, I increment the value of that candidate's vote in the votes dictionary by one.
        votes[row["Candidate"]] += 1

print(f'Total Votes: {totalvotes}')

# I run a for loop through my votes dictionary to get the percentage of total votes for each candidate.
for i in votes:
    # For each candidate in the votes dictionary, we get their votes out of the total votes
    percentage = int(votes[i]) / totalvotes 
    # Then mulitply by 100 to get the percentage
    percentage *= 100
    # And round for good measure
    percentage = round(percentage, 0)
    print(f'{i}: {percentage}00% {votes[i]}')

# For the sake of efficiency, I set this value before running my for loop
highestvotes = max(votes.values())
winnername = None
# This goes through my votes dictionary to assign the winnername variable to the candidate with the most votes
for name, vote in votes.items():
    if vote == highestvotes:
        winnername = name
        print(f'Winner: {winnername}')

# Setting the output for the text file
resultspath = os.path.join("Analysis", "pollresults.txt")

# This writes the text file to show the same results as what is printed in the terminal with a bit more formatting
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