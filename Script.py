import os
import csv

#creating path to read csv file
csvpath = os.path.join('Resources', 'Budget_data.csv')
#establish a variable to count the number of months
num_months = 0
Total = 0    
average = 0
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    #skip the first header row
    header = next(reader)
    first_row = next(reader)
    num_months += 1
    Total += int(first_row[1])

    #loop through each row in the file 
    prev_net = 0
    net_change_list = []
    for row in reader:
        num_months += 1
        ProfLoss = int(row[1])
        Total += ProfLoss
    
    #calculate the average changes
    net_change = int(row[1]) - prev_net
    prev_net = int(row[1])
    net_change_list.append(net_change)

average = sum(net_change_list) / len(net_change_list)

    #print the financial analysis to the console
print("==Financial Analysis==")
print("--------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${Total}")
print(f"Average Change: ${average: .2f}")
    
    # Write the financial analysis to a text file
with open("output.txt", "w") as output_file:
        output_file.write("==Financial Analysis==\n")
        output_file.write("--------------------------\n")
        output_file.write(f"Total Months: {num_months}\n")
        output_file.write((f"Total: {Total}"))
        output_file.write(f"Average Change: {average:.2f}\n")