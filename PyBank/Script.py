import os
import csv

#creating path to read csv file
csvpath = os.path.join('Resources', 'Budget_data.csv')

#establish the variables 
num_months = 0
Total = 0    
average = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999]

#open csv file and loop through rows
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    #skip the first header row and process first row
    header = next(reader)
    first_row = next(reader)
    num_months += 1
    Total += int(first_row[1])

    #loop through each row in the file 
    prev_net = int(first_row[1])
    net_change_list = []
    for row in reader:
        num_months += 1
        ProfLoss = int(row[1])
        Total += ProfLoss
    
        #calculate the profit/loss
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)

        #find the greatest increase and decrease in the profit lis
        if net_change > greatest_increase[1]:
             greatest_increase[0] = row[0]
             greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#calculate average changes
average = sum(net_change_list) / len(net_change_list)

#print the financial analysis
print("==Financial Analysis==")
print("--------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${Total}")
print(f"Average Change: ${average: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
# Write the financial analysis to a text file
with open("output.txt", "w") as output_file:
        output_file.write("==Financial Analysis==\n")
        output_file.write("--------------------------\n")
        output_file.write(f"Total Months: {num_months}\n")
        output_file.write((f"Total: ${Total}\n"))
        output_file.write(f"Average Change: ${average:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")