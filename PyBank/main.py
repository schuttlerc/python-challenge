import os
import csv
csvpath = os.path.join('Resources/budget_data.csv')

rows = []
date = []
profits = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        rows.append(row)
        date.append(row[0])
        profits.append(row[1])

profits_int = [eval(i) for i in profits]

#Calculate the total number of months included in the dataset    
total_months = len(rows)
#Calculate to net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_int)
#Calculate the changes in "Profit/Losses" over the entire period,and then the average of those changes
change =[profits_int[i +1]-profits_int[i] for i in range(total_months - 1)]
average_change = sum(change) / len(change)
#Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(change)
#Calculate the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(change)

gi_index = change.index(greatest_increase)
gd_index = change.index(greatest_decrease)
gi_date = date[gi_index+1]
gd_date = date[gd_index+1]

net_total = "${:,}".format(net_total)
average_change = "${:,.2f}".format(average_change)
greatest_increase = "(${:,})".format(greatest_increase)
greatest_decrease = "(${:,})".format(greatest_decrease)

print("Financial Analysis")
print("----------------------------")
print("Total Months:", total_months)
print("Total:", net_total)
print("Average Change:", average_change)
print("Greatest Increase in Profits:", gi_date, greatest_increase)
print("Greatest Decrease in Profits:", gd_date, greatest_decrease)

out = open("analysis/output.txt", "w")
out.write("Financial Analysis")
out.write("\n----------------------------")
out.write("\nTotal Months: " + str(total_months))
out.write("\nTotal: " + str(net_total))
out.write("\nAverage Change: " + str(average_change))
out.write("\nGreatest Increase in Profits: " + str(gi_date) + " " + str(greatest_increase))
out.write("\nGreatest Decrease in Profits: " + str(gd_date) + " " + str(greatest_decrease))
out.close()
