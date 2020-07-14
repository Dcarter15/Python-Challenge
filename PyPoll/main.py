import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')
votes = []
candidate_list = []
votes_per_candidate = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        votes.append(str(row[2]))
        candidate_list.append(str(row[2]))
    for r in range(len(candidate_list)-1):
        votes_per_candidate.append(candidate_list[1])


print("Election Results")
print("---------------------------------")
print(f"The total amount of votes is ", sum(votes))
print("The vote getter were Khan, Correy, Li, and O'Tooley")
