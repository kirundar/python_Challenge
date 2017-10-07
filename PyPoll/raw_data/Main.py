import os,sys
import subprocess
import glob
from os import path
import sys

def print_both(file, *args):
    toprint = ' '.join([arg for arg in args])
    print (toprint)
    file.write(toprint)

file =open('PyPoll.out.txt', 'w')

total_voted = 0
total_candidate_list = []
uniq_candidate_list = []
vote_count_per_candidate_list = []
avrge_vote_list = []

#Pypoll code
with open('./election_data_2.csv', 'r') as infile:
    infile.readline()  #skipping the first line, Header
    for row in infile:  #looping between rows
        total_voted = total_voted + 1   #counting total rows or voters
        row_index = row.rstrip().split(',')   #spliting the rows to make a list
        total_candidate_list.append(row_index[2])  #puting candidates names including duplicate into a list
    for candidate in total_candidate_list:   # looping between newly created list
        if candidate not in uniq_candidate_list: #applying the condition to get the uniq name
            uniq_candidate_list.append(candidate) #creating new list with uniq names


#print(uniq_candidate_list)
print_both(file,'-------------------------\nElection Results\n-------------------------\nTotal Votes: ' + str(total_voted) + '\n-------------------------\n' )



for vote_count_per_candidate in uniq_candidate_list: # looping between list of candidates names including duplicate
    vote_count_per_candidate_list.append(total_candidate_list.count(vote_count_per_candidate)) #making a list of how many time candidate names came int he list to get the total vote count for each candidate
vote_count_per_candidate_dict = dict(zip(uniq_candidate_list,vote_count_per_candidate_list)) #making a dict with zip between uniq name and their respective count

for keys in vote_count_per_candidate_dict: #taking the output as mentioned on the example
    avrge_vote = (float(vote_count_per_candidate_dict[keys]))/(float(sum(vote_count_per_candidate_dict.values()))) * 100
    avrge_vote_list.append(avrge_vote)


    print_both(file, keys + ' : ' + str("{0:.2f}".format(avrge_vote)) + '%' + '('+str(vote_count_per_candidate_dict[keys])+')\n')


for keys in vote_count_per_candidate_dict:
    if vote_count_per_candidate_dict[keys] == max(vote_count_per_candidate_dict.values()):


        print_both(file,'-------------------------\nWinner: ' + str(keys) + '\n-------------------------')



file.close()