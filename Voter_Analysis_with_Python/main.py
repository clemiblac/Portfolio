# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:20:54 2020

@author: clemi
"""
import os
import csv

#where to find the csv file
data_path=os.path.join("..","PyPoll","Resources","election_data.csv")

#open and read the csv file
with open(data_path) as csvfile:
    election_data=csv.reader(csvfile, delimiter = ',')

    #skipping header row
    next(election_data)
    
    total_votes=0
    candidate_vote=0
    compiled_candidate_list=[]
    candidate_names=[]
    vote_numbers=[]
    Khan_votes=0
    Correy_votes=0
    Li_votes=0
    OTooley_votes=0

    
    #The total number of votes cast
    for votes in election_data:
        total_votes+=1
        
    #A complete list of candidates who received votes
        if votes[2] not in compiled_candidate_list:
            # source (not in) code: https://www.geeksforgeeks.org/python-get-unique-values-list/
           compiled_candidate_list.append(votes[2])
           candidate_names.append(compiled_candidate_list[-1])
           
    #The total number of votes each candidate won
        if votes[2]==candidate_names[0]:
            Khan_votes+=1
        elif votes[2]==candidate_names[1]:
            Correy_votes+=1
        elif votes[2]==candidate_names[2]:
            Li_votes+=1
        elif votes[2]==candidate_names[3]:
            OTooley_votes+=1
            

    #The percentage of votes each candidate won
        if votes[2]==candidate_names[0]:
            Khan_percent=Khan_votes/total_votes
        elif votes[2]==candidate_names[1]:
            Correy_percent=Correy_votes/total_votes
        elif votes[2]==candidate_names[2]:
            Li_percent=Li_votes/total_votes
        elif votes[2]==candidate_names[3]:
            OTooley_percent=OTooley_votes/total_votes  
    
    #The winner of the election based on popular vote.
        vote_numbers=[Khan_votes,Correy_votes,Li_votes,OTooley_votes]
        #calculating the max votes        
        popular_vote=max(vote_numbers)
        
        # candidate names are stored in list "candidate_names"
        #creating a dictionary to combine names and corresponding results
        resultsDict={}
        for name in candidate_names:
            for numbers in vote_numbers:
                resultsDict[name]=numbers
                vote_numbers.remove(numbers)
                break
        """source for convering list to dict:
            https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/""" 
        
        
        """reversing the key and value positions in the dictionary so I can pull winner name
        #by popular vote value"""
        reversed_dict = {}
        for key, value in resultsDict.items():
           reversed_dict[value] = key
        """source for code to reverse key and value positions from dictionary:
            https://realpython.com/iterate-through-dictionary-python/#iterating-through-values"""
    
    """Printing out intermediate results and lists"""
    #printing out candidate list
    print(f"candidate_list : {compiled_candidate_list}")
    print(f"popular_vote : {popular_vote}")
    
    print(f"dictionary: {resultsDict}")
    print(f"reversed dictionary: {reversed_dict}")
    #print(reversed_dict.get(popular_vote))   
    """code for dict.get()---python for everybody, chapter 9, page 110"""
    
    
    #print out results to terminal
    print("                              ")
    print(f"Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"{candidate_names[0]}: {Khan_percent:,.3%} ({Khan_votes})")
    print(f"{candidate_names[1]}: {Correy_percent:,.3%} ({Correy_votes})")
    print(f"{candidate_names[2]}: {Li_percent:,.3%} ({Li_votes})")
    print(f"{candidate_names[3]}: {OTooley_percent:,.3%} ({OTooley_votes})")
    print("-----------------------------")
    print(f"Winner: {reversed_dict.get(popular_vote)}")
    print("-----------------------------")
   

#printing out results to text file
results_path=os.path.join("..","PyPoll","Analysis","PyPoll_Analysis.txt")    
with open(results_path, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------------\n")
    txtfile.write(f"{candidate_names[0]}: {Khan_percent:,.3%} ({Khan_votes})\n")
    txtfile.write(f"{candidate_names[1]}: {Correy_percent:,.3%} ({Correy_votes})\n")
    txtfile.write(f"{candidate_names[2]}: {Li_percent:,.3%} ({Li_votes})\n")
    txtfile.write(f"{candidate_names[3]}: {OTooley_percent:,.3%} ({OTooley_votes})\n")
    txtfile.write("-------------------------------\n")
    txtfile.write(f"Winner: {reversed_dict.get(popular_vote)}\n")
    txtfile.write("-------------------------------\n")
    
    
    
    
    
    
    
    
    