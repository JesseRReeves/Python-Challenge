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
prev_net = 0
change_list = []

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row
    csv_header = next(csv_reader)
    
    # Read through each row of data after the header
    for row in csv_reader:

        # Track the total months
        total_months += 1
        total_net += int(row[1])
        current_profit_loss = int(row[1])
        new_change = current_profit_loss - prev_net
        change_list += [new_change]
        prev_net = int(row[1])
    change_list = change_list[1 : ]
    average_change = sum(change_list)/len(change_list)
    print(average_change)


    # Use prev_net to find the changes in "Profit/Losses"
    
        
     




















 # Organize the test file
    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months : {total_months}")
    print(f"Total: : ($){total_net}")





output_file = os.path.join("Analysis", "budget_analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(str(total_months))