import  os
import csv

filepath = os.path.join("Resources", "budget_data.csv")
#create lists to hold the list of dates
date = []
#creaste a list to hold a list of each months profits
Current_Months_Profits = []
#create a duplicate list of profits to find the change in profits from month to month
Next_Months_Profits = []
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    #remove the header
    csv_header = next(csvreader)
    #create a for loop to store data in the lists
    for row in csvreader:

        date.append(row[0])
        Current_Months_Profits.append(int(row[1]))
        Next_Months_Profits.append(int(row[1]))
    #set a variable to store the length of the date list to find the total months
    totaldate = len(date)
    #set a variable to hold the total sum of profits to find the total made
    totalprofits = sum(Current_Months_Profits)
    #remove the first profit from the duplicate profits list 
    Next_Months_Profits.pop(0)
    #subtract the dublicate profits list from the orginal profits list to make a list of the month to month changes
    profit_change = [Next_Months_Profits[i]- Current_Months_Profits [i] for i in range(min(len(Next_Months_Profits), len(Current_Months_Profits)))]
    #divide the sum of the total profit change by how many months of change there were and round to 2 decimals
    avechange = round(sum(profit_change)/len(profit_change), 2)
    #find the max vaule in the profit_change list to determine the Greatest increase in profits
    inc = max(profit_change)
    #find the min vaule in the profit_change list to determine the Greatest decrease in profits
    dec = min(profit_change)
    #set each analysis to a list
    Months = ["Total Months: ", totaldate]
    Profits = ["Total: ", "$" + str(totalprofits)]
    Change = ["Average Change: ", "$" + str(avechange)]
    Greatest_Increase = ["Greast Increase in Profits: ", str(date[79]) + " " + str(inc)]
    Greatest_Decrease = ["Greatest Decrease in Profits: ", str(date[49]) + " " + str(dec)]
    #zip the lists together
    Financial_Analysis = zip(Months,Profits, Change, Greatest_Increase,Greatest_Decrease)
    # print(Financial_Analysis)
    print("----------------------------")
    print("Total Months: " + str(totaldate))
    print("Total: " + "$" + str(totalprofits))
    print("Average Change: " + "$" + str(avechange)) 
    print("Greast Increase in Profits: " + str(date[79]) + " " + str(inc))
    print("Greatest Decrease in Profits: " + str(date[49]) + " " + str(dec))
    #create an output path
    output_file = os.path.join("analysis", "output.csv")

# open the output file and then write the zipped object to the csv
    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerows(Financial_Analysis)