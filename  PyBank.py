import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as pybank:
    csvreader = csv.reader(pybank, delimiter=',')
    data_change = []
    average_change = 0.0
    csv_header = next(csvreader)
    previous_row = 0
    max_change = ["", 0]
    min_change = ["", 999999999999999]
    total = 0
    revenue = 0 
    month_change = []

    for row in csvreader:
        total = total + 1
        revenue = revenue + int(row[1])
        row_change = int(row[1]) - previous_row
        data_change =   data_change + [row_change]
        previous_row = int(row[1])
        average_change= sum(data_change)/ len(data_change)
        month_change = month_change + [row[1]]

        if (row_change > max_change[1]):
            max_change[0] = row[0]
            max_change[1] = row_change

        if (row_change < min_change[1]):
            min_change[0] = row[0]
            min_change[1] = row_change

print("Financial Analysis")
print("-------------------")
print("Total months: " + str(total))
print("Total Profit/Losses: $" + str(revenue))
print(" Average change: $" + str(average_change))
print("Greatest Increase in profits: " + str(max_change[0]) + " $" + str(max_change[1]))
print("Greatest Decrease in losses: " + str(min_change[0]) + " $" + str(min_change[1]))