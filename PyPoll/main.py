#Import the file and file path
import os
import csv
election_csv = os.path.join("Resources","election_data.csv")

#Print csv to look at the data
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(next(csvreader))
    votes = []
    county = []
    candidates = []
    percentage_votes = []
    khan = []
    correy = []
    li = []
    otooley = []
#vote count
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    total_votes = (len(votes))
    print(total_votes)
#vote per candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
#Percentages
    khan_perc = round(((khan_votes / total_votes)*100),2)
    correy_perc = round(((correy_votes / total_votes)*100),2)
    li_perc = round(((li_votes / total_votes)*100),2)
    otooley_perc = round(((otooley_votes / total_votes)*100),2)
    print(khan_perc)
    print(correy_perc)
    print(li_perc)
    print(otooley_perc)
#Winner options
    if khan_perc > max(correy_perc, li_perc, otooley_perc):
        winner = "Khan"
    elif correy_perc > max(khan_perc, li_perc, otooley_perc):
        winner = "Correy"
    elif li_perc > max(khan_perc, correy_perc, otooley_perc):
        winner = "Li"
    elif otooley_perc > max(khan_perc, correy_perc, li_perc):
        winner = "O'Tooley"


    Results = (
    f"Election Results\n"
    f"-------------------------------------\n" 
    f"Total Votes: {total_votes}\n"
    f"-------------------------------------\n" 
    f"Khan: {khan_perc}% ({khan_votes})\n"
    f"Correy: {correy_perc}% ({correy_votes})\n"
    f"Li: {li_perc}% ({li_votes})/n"
    f"O'Tooley: {otooley_perc}% ({otooley_votes})\n"
    f"-------------------------------------\n" 
    f"Winner: {winner}\n"
    f"-------------------------------------\n"
    )
    file = os.path.join("output","output.txt")
    with open(file, 'w') as writefile:

        writefile.write(Results)