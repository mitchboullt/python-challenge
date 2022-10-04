import  os
import csv

filepath = os.path.join("Resources", "election_data.csv")
#make a list to hold vote data
votes = []
#make a list to hold the candidate data
candidates = []
# candidatenames = []
#set a counter for each candidate
DDcounter = 0
RADcounter = 0
CCScounter = 0
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    #remove the header
    csv_header = next(csvreader)
    #make a for loop to seperate the voter and candidate data
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
    #make a set to find all candidates running
    difcandidates = set(candidates)
    #make a for loop to count how many times each candidate was voted for
    for i in candidates:
        if i == 'Diana DeGette':
            DDcounter = DDcounter + 1
        elif i == 'Raymon Anthony Doane':
            RADcounter = RADcounter + 1
        else:
            CCScounter = CCScounter + 1
    #find the length of the votes list to see how many people voted
    totalvotes = len(votes)
    #set variables to see what percentage of the votes each candidate received
    DDper = round((DDcounter / totalvotes) * 100,3)
    RADper = round((RADcounter / totalvotes) * 100,3)
    CCSper = round((CCScounter / totalvotes) * 100, 3)
#set  poll results to lists
Total_Votes = ["Total Votes: ", str(totalvotes)]
Candidate1 = ["Charles Casper Stockham: ",  str(CCSper) + "% " + "(" + str(CCScounter) + ")"]
Candidate2 = ["Diana DeGette: ", str(DDper) + "% " + "(" + str(DDcounter) + ")"]
Candidate3 = ["Raymon Anthony Doane: ", str(RADper) + "% "+ "(" + str(RADcounter) + ")"]
Winner = ["Winner: ", "Diana DeGette"]
#zip result lists
poll_analysis = zip(Total_Votes, Candidate1, Candidate2, Candidate3, Winner)
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")
print("Charles Casper Stockham: " + str(CCSper) + "% " + "(" + str(CCScounter) + ")")
print("Diana DeGette: " + str(DDper) + "% " + "(" + str(DDcounter) + ")")
print("Raymon Anthony Doane: " + str(RADper) + "% "+ "(" + str(RADcounter) + ")")
print("-------------------------")
print("Winner: Diana DeGette  ")
#create output path
output_file = os.path.join("analysis", "output.csv")

# open the output file and then write the zipped object to the csv
with open(output_file, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerows(poll_analysis)