#This is the PyPoll excercise from the Week 3 Python Module.
#In this script, I will analyze provided town records to reflect:
#   -The total number of votes cast
#   -A complete list of candidates who received votes
#   -The percentage of votes each candidate won
#   -The total number of votes each candidate won
#   -The winner of the election based on popular vote

#Importing modules
import os
import csv

#Opening data file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    #Creating list for data
    candidates = [] #List of candidates
    candcount = []  #Count of candidates's votes

    #Creating my initial list of variables
    totvote = 0

    for row in csvreader:
        
        #Calculating the total number of votes
        totvote = totvote + 1
       
        #Counting the number of votes per candidate
        c = row[2]
        if c not in candidates:
            candidates.append(c)
            candcount.append(1)
        else:
            cindex = candidates.index(c)
            currcount = candcount[cindex]
            candcount[cindex] = currcount + 1

#Formatting the results and finalizing output (i.e. doing percentages and finding winner)
output = []
output.append("-------------------------")
output.append("Election Results")
output.append("-------------------------")
output.append("Total Votes: "+str(totvote))
output.append("-------------------------")
for i, c in enumerate(candidates):
    #Calculating the Percentage of Votes per Candidate
    votes = candcount[i]
    pervote = round((votes/totvote)*100,2)
    
    #Finding the Winner
    votewin = 0
    if votes > votewin:
        winner = c
        votewin = votes
    output.append(c+": "+str(pervote)+"% "+"("+str(votes) +")")
output.append("-------------------------")
output.append("Winner: "+ str(winner))

#Printing and exporting results
export = os.path.join("Analysis", "analysis.txt")
exportfile= open(export, "w")    
for line in output:
    print(line)
    print(line,file=exportfile)

#Export the results
#export = os.path.join("Analysis", "analysis.txt")
#with open(export, "w") as txt_file:
#    txt_file.write(str(output))
    