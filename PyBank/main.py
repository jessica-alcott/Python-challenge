## PyBank

#Import the file and file path
import os
import csv
budget_csv = os.path.join("Resources","budget_data.csv")

#Print csv to look at the data
with open(budget_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  print(next(csvreader))
  month = []
  revenue = []
  revenue_change = []
  monthly_change = []


#![Revenue](Images/revenue-per-lead.png)
#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. # You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). # The dataset is composed of two columns: `Date` and `Profit/Losses`. # (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#* Your task is to create a Python script that analyzes the records to calculate each of the following:
#set the heading referenced below
 
  #* The total number of months included in the dataset
#* The net total amount of "Profit/Losses" over the entire period
  #* The average of the changes in "Profit/Losses" over the entire period
#Months
  for row in csvreader:
    month.append(row[0])
    revenue.append(row[1])
  print(len(month))
  #Revenue
  revenue_int = map(int,revenue)
  total_revenue = (sum(revenue_int))
  print(total_revenue)
  #Avg change
  i = 0
  for i in range(len(revenue) -1):
    profit_loss = int(revenue[i+1]) - int(revenue[i])
    revenue_change.append(profit_loss)
  Total = sum(revenue_change)
  monthly_change = Total / len(revenue_change)
  print(monthly_change)

  #Greatest Increase
  profit_increase = max(revenue_change)
  print(profit_increase)
  j = revenue_change.index(profit_increase)
  month_increase = month [j+1]

  #Greatest Decrease
  profit_decrease = min(revenue_change)
  print(profit_decrease)
  k = revenue_change.index(profit_decrease)
  month_increase = month [k+1]  

  Results = (
    f'Financial Analysis\n'
    f' ----------------------------\n'
    f"Total number of months:  +str(len(month))\n"
    f"Total: $ (total_revenue)\n"
    f"Average Change: $ +str(monthly_change)\n"
    f"Greatest Increase: $ +str(profit_increase)\n"
    f"Greatest Decrease: $ +str(profit_decrease)\n"
  )


  file = os.path.join("output","output.txt")
  with open(file, 'w') as writefile:

      writefile.write(Results)
#* As an example, your analysis should look similar to the one below:

 # ```text
 # Financial Analysis
 # ----------------------------
 # Total Months: 86
  #Total: $38382578
 # Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
 # Greatest Decrease in Profits: Sep-2013 ($-2196167)
 # `
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.