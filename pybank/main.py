import os
import csv

# Set path to collect data from the resources folder.
pybank_csv = os.path.join("Resources", "budget_data.csv")

#Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Read the header row
    csv_header = next(csv_reader)
    print(f"Header {csv_header}")
   
    # Define total_months
    total_months = 0
   
    #Read through each row of data after the header
    for row in csv_reader:

        #Track the total
        total_months += 1
        print(total_months)


























output_file = os.path.join("Analysis", "budget_analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(str(total_months))