import os,sys
import subprocess

date_list = []
rev_list = []
month = 0
Khan_count= 0
change_btw_months_list = []

def print_both(file, *args):
    toprint = ' '.join([arg for arg in args])
    print (toprint)
    file.write(toprint)

file =open('PyBank.out.txt', 'w')

with open('./budget_data_2.csv', 'r') as infile:
    infile.readline()       #skipping first line
    for row in infile:      #Looping between rows
        month = month + 1   # taking the count of total row to get the total months
        value = row.rstrip().split(',')  #making each row into a list to index
        date_list.append(value[0])      #creating new list with the help of indexing
        rev_list.append(int(value[1]))  #creating new list with the help of indexing
    for chg_ind in range(len(rev_list)): #looping the index of the list rev_list to find the montly change in rev
        if chg_ind != (len(rev_list)-1): #skipping the last index or item
            if rev_list[chg_ind] < 0:    #now calculating to avoid the wrong '-' calculation
                change_btw_months = rev_list[chg_ind + 1] + rev_list[chg_ind]
            elif rev_list[chg_ind + 1] < 0: #now calculating to avoid the wrong '-' calculation
                change_btw_months = rev_list[chg_ind + 1] + rev_list[chg_ind]
            else:
                change_btw_months = rev_list[chg_ind + 1] - rev_list[chg_ind]
            change_btw_months_list.append(change_btw_months) #creating new list with monthly change with the help of index value calculation


print_both(file,'\nFinancial Analysis\n----------------------------\nTotal Months: ' + str( month))
print_both(file,'\nTotal Revenue: $'+ str(sum(rev_list)))
#print('The change in revenue between months over the entire period',change_btw_months_list)
print_both(file,'\nAverage Revenue Change: $'+ str(sum(change_btw_months_list)/len(change_btw_months_list)))
#print ('max rev:', max(rev_list))
#print ('min rev:', min(rev_list))

for max_ind in range(len(rev_list)):
    if rev_list[max_ind] == max(rev_list):
        print_both(file,'\nGreatest Increase in Revenue: ' + str(date_list[max_ind]) +' ($'+str(rev_list[max_ind])+')')

for min_ind in range(len(rev_list)):
    if rev_list[min_ind] == min(rev_list):
        print_both(file,'\nGreatest Decrease in Revenue:' + str(date_list[min_ind]) + ' ($'+str(rev_list[min_ind])+')')


file.close()