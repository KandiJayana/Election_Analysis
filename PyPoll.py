#The data we need to retrieve.
# 1. The total number of voter cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidates won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# Import the datetime class from the datetime module.
# Add our dependencies.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')
# To do: perform analysis.
# Close the file.
election_data.close()
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)
