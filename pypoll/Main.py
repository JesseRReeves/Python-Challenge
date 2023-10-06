# Import operating system
import os

# Import module for reading csv files
import csv

#Set path to collect data from the resources folder
pypoll_csv = os.path.join("Resources", "election_data.csv")

# Define total number of votes
total_votes = 0

# Define list of candidates
candidates = {}


# Open and read csv
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row
    csv_header = next(csv_reader)

    # Loop through each row of data after the header
    for row in csv_reader:
        
        # Track the total votes
        total_votes += 1
        
        # Find the total votes
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else: 
            candidates[row[2]] = 1
highest_votes = 0

# Set up where to write text within a specific text file
output_file = os.path.join("Analysis", "election_results.txt")
with open(output_file, "w") as txt_file:
    
    # Write the text file answers 
    txt_file.write("Election Results\n\n")
    txt_file.write("-------------------------\n\n")
    txt_file.write(f"Total Votes: {total_votes}\n\n")
    txt_file.write("-------------------------\n\n") 
    
    # Find out the winner of the election
    for candidate in candidates.keys():
        if candidates[candidate] > highest_votes:
            winner = candidate
            highest_votes = candidates[candidate]
        # Find out the percentage of total votes per candidate
        txt_file.write(f"{candidate}: {round(candidates[candidate]/total_votes * 100, 3)}% ({candidates[candidate]})\n\n")
    txt_file.write("-------------------------\n\n")
    txt_file.write(f"Winner: {winner}\n\n")
    txt_file.write("-------------------------")
            


        









        
        

