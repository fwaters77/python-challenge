import os

import csv

#Import CSV file
csvpath =os.path.join("PyPoll", "election_data_1.csv")
csvpath =os.path.join("PyPoll", "election_data_2.csv")

#make list to store votes
total_votes = []
candidate_list = []
vote_percentage = []
candidate_votes = []
winner = []

#Open CSV

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Loop through rows
    #The total number of votes cast
    #vote counter
    voterID = 0
    for row in csvreader:

        voterID += 1

        #Add to voterID list.
        total_votes.append(voterID)
    len(total_votes)
    print(len(total_votes))
    
   

#A complete list of candidates who received votes
    
    
    for row in csvreader:
        #Add candidate to candidate_list
        candidate_list.append(row[2])
        #Remove the duplicates
        candidates = []
        for candidate in candidate_list:
            if candidate not in candidates:
                candidates.append(candidate)
            print(candidates)   
