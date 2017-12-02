# In this challenge, you are tasked with creating a Python script for analyzing the financial records 
# of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The total amount of revenue gained over the entire period
# The average change in revenue between months over the entire period
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period

#dependencies
#os module will allow us to create file paths across operating systems
import os
import csv

#create csv file path using os module to read file with
budget_data_path = os.path.join ('raw_data', 'budget_data_1.csv')

#create text file path to write file to
budget_data_path_out = os.path.join('budget_data_test_today.txt')

#create variables to store the data
total_months = 0
total_revenue = 0
previous_month_revenue = 0
revenue_change_stored_list = []
revenue_average_change = 0
greatest_increase_list = ["",0] #store smallest number
greatest_decrease_list = ["",10000000000] #store largest number (hard coded - investigate alternatives)

#improved reading with csv module
with open(budget_data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row that is a header row so it doesn't pull into total counts/sums
    next(csvreader, None)
    
    #begin for loop, which will continue running until file reads last row
    for row in (csvreader):

        #calculate total number of months in dataset
        total_months = total_months + 1

        #calculate total revenue of all records in dataset
        total_revenue = (total_revenue) + int(row[1])

        #calculate revenue change between the months in dataset
        revenue_change = int(row[1]) - previous_month_revenue
        previous_month_revenue = int(row[1])
        revenue_change_stored_list = revenue_change_stored_list + [revenue_change]

        #calculate the average revenue change
        revenue_average_change = sum(revenue_change_stored_list)/len(revenue_change_stored_list)
        rounded_revenue_average_change = round(revenue_average_change,2)

        #calculate the greatest increase
        if (revenue_change > greatest_increase_list[1]):
            greatest_increase_list[0] = row[0]
            greatest_increase_list[1] = revenue_change

        #calculate the decrease increase
        if (revenue_change < greatest_decrease_list[1]):
            greatest_decrease_list[0] = row[0]
            greatest_decrease_list[1] = revenue_change

# # print out each statement and convert to string to combine values
# print("Financial Analysis")
# print("---------------------------------")
# print("Total Months: "+ str(total_months))
# print("Total Revenue: $"+ str(total_revenue))
# print("Average Revenue Change: $"+ str(rounded_revenue_average_change))
# print("Greatest Increase in Revenue: "+ str(greatest_increase_list[0]) + " ($" + str(greatest_increase_list[1]))
# print("Greatest Decrease in Revenue: "+ str(greatest_decrease_list[0]) + " ($" + str(greatest_decrease_list[1]))

# store all the print statement sinto a single variable so you can write to output file
results = (
"\nFinancial Analysis\n"
"---------------------------------\n"
"Total Months: "+ str(total_months) + "\n"
"Total Revenue: $"+ str(total_revenue) + "\n"
"Average Revenue Change: $"+ str(rounded_revenue_average_change) + "\n"
"Greatest Increase in Revenue: "+ str(greatest_increase_list[0]) + " ($" + str(greatest_increase_list[1]) + ")\n"
"Greatest Decrease in Revenue: "+ str(greatest_decrease_list[0]) + " ($" + str(greatest_decrease_list[1]) + ")\n")

#this will print results stored in variable to output of terminal for assignment results
print(results)

#write all the content of print statement to text file (output path)
with open(budget_data_path_out, "w") as txt_file:
    txt_file.write(results)