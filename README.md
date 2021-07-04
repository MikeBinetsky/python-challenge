# python-challenge
This is for the third homework submission. Python Challenge.

For this challenge there are two parts, PyBank and PyPoll.

PYBANK
-----------------------------------------------------------
In PyBank we had a .csv file that contained dates and associated profit/loss numbers.
Our goal was to find the below:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

  To do this, I opened the original file and converted it to a dictionary for easier use. 

  I decided to use a dictionary over a list interpretation as personal preference. I prefer the functionality of dictionaries over lists.

  From there I use a for loop to check through each row of my data adding that row's profit's to a total profits variable to return the net total profits/losses.

  In this same loop, I add to lists containing the monthly change for that month from the previous month, as well as the current month's date.

  Finally, before returning all the values I need. I do another for loop to check each part of my monthly profits/losses change list to see if it is the highest or lowest value and I return the index of each of those values since it matches with the date.

  I print out all of the results, then write those results to a new .txt file.


PYPOLL
  ----------------------------------------------------------------------------------
In PyPoll we had a .csv file that contained a VoterID, County, and Candidate (Vote)
Our goal was to find the below

  *  The total number of votes cast

  *  A complete list of candidates who received votes

  *  The percentage of votes each candidate won

  *  The total number of votes each candidate won

  *  The winner of the election based on popular vote.

I opened the original file and converted it to a dictionary for easier use, again using dictionary as personal preference as I like the functionality of them over lists.

From there, I used a for loop to count the total number of votes cast adding 1 to a total votes variable every iteration of the loop.

To get the candidate names I used an if statement in my for loop that checks if that candidate's name is not in the dictionary I created so far to hold the candidate names and their votes. If it wasn't, I added their name to the dictionary with a starting vote count of 0

Then to close out the loop I iterate the value of that candidate key in my dictionary by 1 to count that as a vote in their favor.

to get the percentage of votes, I use another quick for loop going through my dictionary. I take the number of votes for a given candidate, divide by the total votes, multiple by 100, then round it off to get the percentage for each candidate.

Lastly, before writing my results to a text file, I get the name of the winner based on the number of votes and store it in a variable called winnername to print later.

I print all the results and write those to a new .txt file.