# Import operating system
import os

# Import module for reading csv files
import csv

#Set path to collect data from the resources folder
pypoll_csv = os.path.join("Resources", "election_data.csv")

# Define total number of votes
total_votes = 0

# Define list of candidates
candidates = [""]

# Define percentage of votes each candidate won
percentage_of_votes_each_candidate = 0

# Define total number of votes each candidate won
total_number_of_votes = 0

# Define the winner of the election based on popular vote
Winner = [""]

with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row
    csv_header = next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        # Track the total votes
        total_votes += 1
        
        

