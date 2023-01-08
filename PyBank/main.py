import os
import csv
import statistics
csvpath = os.path.join('Resources', 'budget_data.csv')
# Open the CSV file and read the rows into a list
with open(csvpath,"r")as f:
    rows = list(csv.reader(f))
   


# Get the header row and the data rows
header_row = rows[0]
data_rows = rows[1:]

# Find the column indices for the "month_year" and "profit_loss" columns
month_year_index = header_row.index("Date")
profit_loss_index = header_row.index("Profit/Losses")

# Extract the month_year and profit_loss values from the data rows
month_years = [row[month_year_index] for row in data_rows]
profit_losses = [int(row[profit_loss_index]) for row in data_rows]

# Calculate the total number of months
num_months = len(set(month_years))

# Calculate the net total of profit/losses
net_total = sum(profit_losses)

# Calculate the changes in profit/losses
changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses))]

# Calculate the average change in profit/losses
average_change = statistics.mean(changes)

# Find the greatest increase in profits
max_profit = max(profit_losses)
max_month = month_years[profit_losses.index(max_profit)]

# Find the greatest decrease in profits
min_profit = min(profit_losses)
min_month = month_years[profit_losses.index(min_profit)]

# Print the results
print("Total number of months:", num_months)
print("Net total of profit/losses:", net_total)
print("Average change in profit/losses:", average_change)
print("Greatest increase in profits:", max_month, max_profit)
print("Greatest decrease in profits:", min_month, min_profit)

output_path = os.path.join("Analysis",'results.txt')
with open(output_path, 'w') as f:
    f.write("Total number of months: " + str(num_months) + "\n")
    f.write("Net total of profit/losses: " + str(net_total) + "\n")
    f.write("Average change in profit/losses: " + str(average_change) + "\n")
    f.write("Greatest increase in profits: " + max_month + " " + str(max_profit) + "\n")
    f.write("Greatest decrease in profits: " + min_month + " " + str(min_profit) + "\n")



