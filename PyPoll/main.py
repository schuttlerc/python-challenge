import os
import csv
csvpath = os.path.join('Resources/election_data.csv')

rows = []
ballot_id = []
county = []
candidate = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        rows.append(row)
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Calculate the total number of votes cast
total_votes = len(rows)

#Provide a complete list of candidates who received votes
set_candidate = set(candidate)
list_candidate = list(set_candidate)
list_candidate.sort()
candidate1 = list_candidate[0]
candidate2 = list_candidate[1]
candidate3 = list_candidate[2]

#Calculate the total number of votes each candidate won
candidate1_count = candidate.count(candidate1)
candidate2_count = candidate.count(candidate2)
candidate3_count = candidate.count(candidate3)

#Calculate the the percentage of votes each candidate won
candidate1_percentage = candidate1_count / total_votes * 100
candidate2_percentage = candidate2_count / total_votes * 100
candidate3_percentage = candidate3_count / total_votes * 100

#Determine the winner of the election based on popular vote
candidates = [candidate1,candidate2,candidate3]
candidate_counts = [candidate1_count,candidate2_count,candidate3_count]
most_votes = max(candidate_counts)
most_votes_index = candidate_counts.index(most_votes)
winner = candidates[most_votes_index]

total_votes = "{:,}".format(total_votes)
candidate1 = "{}:".format(candidate1)
candidate2 = "{}:".format(candidate2)
candidate3 = "{}:".format(candidate3)
candidate1_count = "({:,})".format(candidate1_count)
candidate2_count = "({:,})".format(candidate2_count)
candidate3_count = "({:,})".format(candidate3_count)
candidate1_percentage = "{:.3f}%".format(candidate1_percentage)
candidate2_percentage = "{:.3f}%".format(candidate2_percentage)
candidate3_percentage = "{:.3f}%".format(candidate3_percentage)

print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
print(candidate1,candidate1_percentage, candidate1_count)
print(candidate2,candidate2_percentage, candidate2_count)
print(candidate3,candidate3_percentage, candidate3_count)
print("-------------------------")
print("Winner:", winner)
print("-------------------------")

out = open("analysis/output.txt", "w")
out.write("Election Results")
out.write("\n-------------------------")
out.write("\nTotal Votes: " + str(total_votes))
out.write("\n-------------------------")
out.write("\n" + str(candidate1) + " " + str(candidate1_percentage) + str(candidate1_count))
out.write("\n" + str(candidate2) + " " + str(candidate2_percentage) + str(candidate2_count))
out.write("\n" + str(candidate3) + " " + str(candidate3_percentage) + str(candidate3_count))
out.write("\n-------------------------")
out.write("\nWinner: " + str(winner))
out.write("\n-------------------------")
out.close()