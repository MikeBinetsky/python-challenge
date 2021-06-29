# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv
#importing statistics as well in order to more easily calculate the mean
import statistics

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
bankpath = os.path.join("Resources", "budget_data.csv")

# Setting the month total to zero since this can be increased by 1 in the for loop later
monthtotal = 0

# Same thing here. This will be increased in the loop to print later
totalprofit = 0

# This is an empty list that will be appended in the loop to calculate the monthly change and add that change to this list to do calculations on later
monthlychange = []
monthlylist = []

#  These two are here to help calculate the monthly change
currentmonthamount = 0
# the lastmonthamount will start as "none" so that in the first iteration of the loop it won't count any change and disrupt the data
lastmonthamont = None

# First we open the file
with open(bankpath) as bankfile:
    # This is converting the file from a csv into a dicitonary. I personally like dictionaries more than lists.
    bankreader = csv.DictReader(bankfile)
    for row in bankreader:
        # First, we set the current month's profit and losses into the currentmonthamount to be used later
        currentmonthamount = int(row['Profit/Losses'])
        # Then we iterate the monthly total by one to return later
        monthtotal += 1
        # The total profit starts at 0 and is added to this total profit to be returned later
        totalprofit += currentmonthamount
        # This if does a check to see if the last month amount is empty.
        if lastmonthamont != None:
            # Take the current month's amount minus the last month's amount to find the difference and add it to the monthly change list
            monthlychange.append(currentmonthamount - lastmonthamont)
            monthlylist.append(row['Date'])
            # If the last month's profit/losses is empty, this gets skipped since there can be no change if there has been no change. Ya'know?
        #Finally, set the last month's amount to the current month's amount to be used in the next iteration of row
        lastmonthamont = currentmonthamount

print(f'Total Months = {monthtotal}')
print(f'Total Profits = {totalprofit}')
print(f' Average Monthly Change = {round(statistics.mean(monthlychange), 2)}')

# Okay this one is a bit weird. 

# First I set up two new variables: maxmonth and minmonth and set them both to None or Null
maxmonth = None
minmonth = None
# Let's start a loop to go through each item in monthlychange --> The list we added the changes from month to month
for month in monthlychange:
    # for each entry in my monthlychange list I check to see if it's the highest value in the entire list. 
    if month == max(monthlychange):
        # If it is, I grab the index of that value
        maxmonth = monthlychange.index(month)
    # for each entry in my monthlychange list I check to see if it's the highest value in the entire list. 
    if month == min(monthlychange):
        # If it is, I grab the index of that value
        minmonth = monthlychange.index(month)

print(f'Greatest Increase in profits: {monthlylist[maxmonth]} {max(monthlychange)}')
print(f'Greatest Decrease in profits: {monthlylist[minmonth]} {min(monthlychange)}')

resultspath = os.path.join("Analysis", "bankresults.txt")

with open(resultspath, 'w') as results:
    results.write("Financial Analysis\n")
    results.write("------------------\n")
    results.write(f"Total Months: {monthtotal}\n")
    results.write(f"Total Profits/Losses: {totalprofit}\n")
    results.write(f"Average Change: {round(statistics.mean(monthlychange), 2)}\n")
    results.write(f'Greatest Increase in profits: {monthlylist[maxmonth]} {max(monthlychange)}\n')
    results.write(f'Greatest Decrease in profits: {monthlylist[minmonth]} {min(monthlychange)}')