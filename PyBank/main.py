# Importing os for relative file pathing and importing csv to help read csv files!
import os
import csv

# using the os.path.join to make the relative path of the budget_data.csv file. This should be able to be used universally regardless of system
bankpath = os.path.join("Resources", "budget_data.csv")

# Setting the month total to zero since this can be increased by 1 in the for loop later
monthtotal = 0

# Same thing here. This will be increased in the loop to print later
totalprofit = 0

# This is an empty list that will be appended in the loop to calculate the monthly change and add that change to this list to do calculations on later
monthlychange = []

# These are here to store values later in order to calculate change
lastmonth = 0

with open(bankpath, newline='') as bankfile:
    bankreader = csv.DictReader(bankfile)
    for row in bankreader:
        monthtotal += 1
        totalprofit += int(row['Profit/Losses'])
        monthlychange.append(int(row['Profit/Losses']) - lastmonth)


# print(monthtotal)
# print(totalprofit)
print(monthlychange)