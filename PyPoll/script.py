import os
import csv

#creating path to read csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#establish the variables
total_votes = 0
candidate_list = []
candidate_votes = {}
winner_votes = 0
winner = ""

#open csv file and loop through rows
with open(csvpath) as election_data:
    reader = csv.reader(election_data, delimiter=',')

    #skip the first header row and process first row
    header = next(reader)

    #loop through each row in the file
    for row in reader:
        total_votes += 1

        #get candidate name and add new ones to the list
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        
        #add candidate votes
        candidate_votes[candidate_name] += 1

#print the election results
print("==Election Results==")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_list:
    votes = candidate_votes[candidate]
    percent = "{:.3%}".format(votes / total_votes)
    print(f"{candidate}: {percent} ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#write the election results to a text file
with open("output.txt", "w") as output_file:
    output_file.write("==Election Results==\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidate_list:
        votes = candidate_votes[candidate]
        percent = "{:.3%}".format(votes / total_votes)
        output_file.write(f"{candidate}: {percent} ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")