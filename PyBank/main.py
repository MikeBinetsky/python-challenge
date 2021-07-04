# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv
#importing statistics as well in order to more easily calculate the mean
import statistics

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
bankpath = os.path.join("Resources", "budget_data.csv")

# Same thing here. This will be increased in the loop to print later
totalProfit = 0

# This is an empty list that will be appended in the loop to calculate the monthly change and add that change to this list to do calculations on later
monthlyChange = []
monthlyList = []

#  These two are here to help calculate the monthly change
currentMonthAmount = 0
# the lastmonthamount will start as "none" so that in the first iteration of the loop it won't count any change and disrupt the data
lastMonthAmont = None

# First we open the file
with open(bankpath) as bankfile:
    # This is converting the file from a csv into a dicitonary. I personally like dictionaries more than lists.
    bankreader = csv.DictReader(bankfile)
    for row in bankreader:
        # First, we set the current month's profit and losses into the currentMonthAmount to be used later
        currentMonthAmount = int(row['Profit/Losses'])
        # Then we iterate the monthly total by one to return later
        # The total profit starts at 0 and is added to this total profit to be returned later
        totalProfit += currentMonthAmount
        # This if does a check to see if the last month amount is empty.
        if lastMonthAmont != None:
            # Take the current month's amount minus the last month's amount to find the difference and add it to the monthly change list
            monthlyChange.append(currentMonthAmount - lastMonthAmont)
            monthlyList.append(row['Date'])
            # If the last month's profit/losses is empty, this gets skipped since there can be no change if there has been no change. Ya'know?
        #Finally, set the last month's amount to the current month's amount to be used in the next iteration of row
        lastMonthAmont = currentMonthAmount

# The monthly list is the number of months there was change. Since the only month without change was the first we take the length of the month list and add 1.
monthTotal = len(monthlyList) + 1

print(f'Total Months = {monthTotal}')
print(f'Total Profits = {totalProfit}')
print(f' Average Monthly Change = {round(statistics.mean(monthlyChange), 2)}')

# Okay this one is a bit weird. 
# First I set up two new variables: maxMonth and minMonth and set them both to None or Null
maxMonth = None
minMonth = None
maxchange = max(monthlyChange)
minchange = min(monthlyChange)
# Let's start a loop to go through each item in monthlyChange --> The list we added the changes from month to month
for month in monthlyChange:
    # for each entry in my monthlyChange list I check to see if it's the highest value in the entire list. 
    if month == maxchange:
        # If it is, I grab the index of that value
        maxMonth = monthlyChange.index(month)
    # for each entry in my monthlyChange list I check to see if it's the highest value in the entire list. 
    if month == minchange:
        # If it is, I grab the index of that value
        minMonth = monthlyChange.index(month)

print(f'Greatest Increase in profits: {monthlyList[maxMonth]} {maxchange}')
print(f'Greatest Decrease in profits: {monthlyList[minMonth]} {minchange}')

# This is defining the outputh path for the new .txt file
resultspath = os.path.join("Analysis", "bankresults.txt")

# I open the output file with 'w' defined so as to write to the file rather than read it
with open(resultspath, 'w') as results:
    # Here I write the output that I have pritned above. The /n at the end of the lines creates a new line in the text file
    results.write("Financial Analysis\n")
    results.write("------------------\n")
    results.write(f"Total Months: {monthTotal}\n")
    results.write(f"Total Profits/Losses: {totalProfit}\n")
    results.write(f"Average Change: {round(statistics.mean(monthlyChange), 2)}\n")
    results.write(f'Greatest Increase in profits: {monthlyList[maxMonth]} {max(monthlyChange)}\n')
    results.write(f'Greatest Decrease in profits: {monthlyList[minMonth]} {min(monthlyChange)}')