# Import operating system
import os

# Import module for reading csv files
import csv

# Set path to collect data from the resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

 # Define total_months
total_months = 0

# Define net Total profits/losses
total_net = 0

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row
    csv_header = next(csv_reader)
    

    first_row = next(csv_reader)
   
    # Track the total months
    total_months += 1
    

   
    # Read through each row of data after the header
    for row in csv_reader:

        # Track the total months
        total_months += 1
        total_net += int(row[1])
    print(total_net)

    
        
     


























output_file = os.path.join("Analysis", "budget_analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(str(total_months))