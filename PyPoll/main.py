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

