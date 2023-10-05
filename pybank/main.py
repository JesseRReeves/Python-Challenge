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

# Define previous net
prev_net = 0

# Define the change within the list
change_list = []

# Define greatest_increase
greatest_increase = ["", 0]

#Define greatest_decrease
greatest_decrease = ["", 99999999999999]

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row
    csv_header = next(csv_reader)
    
    # Read through each row of data after the header
    for row in csv_reader:

        # Track the total months
        total_months += 1
       
        # Find the total net profit
        total_net += int(row[1])
       
        # Set variables to find the change in profits/losses
        current_profit_loss = int(row[1])
       
        # Calculate the new change 
        net_change = current_profit_loss - prev_net
       
        # Add the new change to our list within the loop
        change_list += [net_change]

        # Set prev_net to go down the column
        prev_net = int(row[1])
       
        # Find the greatest increase in profits, including what month
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            
        # Find the greatest decrease in profits, including what month
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
            
    # Slice out the first index 0 in the change_list 
    change_list = change_list[1 : ]

    # Calculate the average change of the profits/losses
    (average_change) = sum(change_list)/len(change_list)

output_file = os.path.join("Analysis", "budget_analysis.txt")
with open(output_file, "w") as txt_file:
   
    # Organize the text file
    txt_file.write("Financial Analysis\n")
    txt_file.write("\n")
    txt_file.write("------------------------------------\n")
    txt_file.write("\n")
    txt_file.write(f"Total Months: : {total_months}\n")
    txt_file.write("\n")
    txt_file.write(f"Total: : ($){total_net}\n")
    txt_file.write("\n")
    txt_file.write(f"Average Change: : {average_change:.2f}\n")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: : {greatest_increase}\n")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: : {greatest_decrease}\n")





    


    
    
        
     
























