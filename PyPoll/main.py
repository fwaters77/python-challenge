#Import election_data_2
import os

import csv

#Import CSV file
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
            
    #The total number of votes each candidate won
    #Correy
    correy = 0
    correy_total =[]
    for row in csvreader:
        #Vote count for Correy.
        correy += 1 
        #Add to Correy vote total.
        correy_total.append(correy)

     #Khan
     khan = 0
     khan_total =[]
     for row in csvreader:
        #Vote count for Khan.
        khan += 1 
        #Add to Khan vote total.
        khan_total.append(khan)

     #Li
     li = 0
     li_total =[]
     for row in csvreader:
        #Vote count for Li.
        li += 1 
        #Add to Li vote total.
        li_total.append(li)

     #O'Tooley
     otooley = 0
     otooley_total =[]
     for row in csvreader:
        #Vote count for Correy.
        otooley += 1 
        #Add to O'Tooley vote total.
        otooley_total.append(otooley)

#The percentage of votes each candidate won
#Correy vote percentage.
percentageC = correy/voterID
#Add to vote percentage list.
vote_percentage.append(percentageC)
#Khan vote percentage.
percentageK = khan/voterID
#Add to vote percentage list.
vote_percentage.append(percentageK)
#Li vote percentage.
percentageL = li/voterID
#Add to vote percentage list.
vote_percentage.append(percentageL)
#O'Tooley vote percentage
percentageO = otooley/voterID 
#Add to vote percentage list.
vote_percentage.append(percentageO)


#The winner of the election based on popular vote.

totalVotes = {
  
}

#Write data to file.

#Specify the file to write to.
#output_file = open("election_data_final.txt", "w")

# Write the header row
    #writer.writerow(["Total Votes","Candidates"])
    # Write in zipped rows
    #writer.writerows(total_votes,candidates)
    
    
    
    
#Import election_data_1
import os

import csv

#Import CSV file
csvpath =os.path.join("PyPoll", "election_data_1.csv")

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
            
    #The total number of votes each candidate won
    #Vestal
    vestal = 0
    vestal_total =[]
    for row in csvreader:
        #Vote count for vestal.
        vestal += 1 
        #Add to vestal vote total.
        vestal_total.append(vestal)

     #Torres
     torres = 0
     torres_total =[]
     for row in csvreader:
        #Vote count for Torres.
        torres += 1 
        #Add to torres vote total.
        torres_total.append(torres)

     #Seth
     seth = 0
     seth_total =[]
     for row in csvreader:
        #Vote count for Seth.
        seth += 1 
        #Add to Seth vote total.
        seth_total.append(seth)

     #Cordin
     cordin = 0
     cordin_total =[]
     for row in csvreader:
        #Vote count for Cordin.
        cordin += 1 
        #Add to Cordin vote total.
        cordin_total.append(cordin)

#The percentage of votes each candidate won
#vestal vote percentage.
percentageV = vestal/voterID
#Add to vote percentage list.
vote_percentage.append(percentageV)
#torres vote percentage.
percentageT = torres/voterID
#Add to vote percentage list.
vote_percentage.append(percentageT)
#Seth vote percentage.
percentageS = seth/voterID
#Add to vote percentage list.
vote_percentage.append(percentageS)
#Cordin vote percentage
percentageC = cordin/voterID 
#Add to vote percentage list.
vote_percentage.append(percentageC)


#The winner of the election based on popular vote.

totalVotes = {
  
}

#Write data to file.

#Specify the file to write to.
#output_file = open("election_data_final.txt", "w")

# Write the header row
    #writer.writerow(["Total Votes","Candidates"])
    # Write in zipped rows
    #writer.writerows(total_votes,candidates)    
    
    
    
