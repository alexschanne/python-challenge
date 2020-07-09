#This is the PyBank excercise from the Week 3 Python Module.
#In this script, I will analyze provided company records to reflect:
#   -Total number of months in dataset
#   -Net total amount of Profit/Losses over entire period
#   -Average of changes in Profit/Losses over entire period
#   -Greatest increase in profits (date and amount)
#   -Greatest decrease in losses (date and amount)

#Importing modules
import os
import csv

#Opening data file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Creating my initial list of variables
    month = 0       #Number of months
    netrev = 0      #Net Revenue
    prevrev = 0     #The previous month's revenue- needed for delta calculation
    totdelta = 0    #Total Delta of Profit/Losses
    greatinc = 0    #The greatest increase in revenue
    greatdec = 0    #The greatest decrease in revenue

    #Creating a loop to go through the data

    for row in csvreader:
        
        #Calculate Month
        month = month + 1

        #Calculate Net Profit/Loss 
        rev = int(row[1])
        netrev = netrev + rev

        #Finding total change in revenue
        revdelt = rev - prevrev #one month's change in revenue
        totdelta = totdelta + revdelt    #total change
        prevrev = rev
        
        #Finding the Greatest Delta Profit/Losses
        if revdelt > greatinc:              #This will update with each
                greatinc = revdelt          #iteration of the loop 
                greatincdate = row[0] 

        if revdelt < greatdec:
                greatdec = revdelt
                greatdecdate = row[0]

    #Calculate Average Profit/Loss Delta
    avgrev = totdelta/month


    #Print the results
    output= (
    "Financial Analysis"+"\n"
    "----------------------------"+"\n"
    f"Total Months {month}\n"
    f"Total: ${rev}\n"
    f"Average  Change: ${avgrev}]\n"
    f"Greatest Increase in Profits: {greatincdate} ${greatinc}\n"
    f"Greatest Decrease in Profits: {greatdecdate} ${greatdec}\n"
    )

    print(output)

    #Export the results
    export = os.path.join("Analysis", "analysis.txt")
    with open(export, "w") as txt_file:
        txt_file.write(output)
