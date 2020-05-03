# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:19:57 2020

@author: clemi
"""
import os
import csv
import numpy as np

#where to find the csv file
data_path=os.path.join("..","PyBank","Resources","budget_data.csv")

#open and read the csv file
with open(data_path) as csvfile:
    data_reader=csv.reader(csvfile, delimiter = ',')

    #skipping header row
    next(data_reader)

    #declaring variables and lists
    total_months=0 
    
    netprofit=0
    
    sum_of_changes=0
    
    current_profit=0
    
    greatest_increase=0
    
    current_loss=0
    
    greatest_decrease=0
    
    original_list=[]
    change_list=[]
    date_list=[]
    
    for records in data_reader:
        #The total number of months included in the dataset
        total_months+=1
        
        #The net total amount of "Profit/Losses" over the entire period
        netprofit+=int(records[1])
    
        #The average of the changes in "Profit/Losses" over the entire period  
        """to do this find the difference between each individual row, 
        add them up and divide by total_month-1"""
        
        """first, convert values in profit/loss column to a list"""
        original_list.append(int(records[1]))
            
        """second, find the successive difference of items in the list"""
        change = [original_list[i + 1] - original_list[i] for i in range(len(original_list)-1)]
        """ source for "change" code:
        https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/"""
        
        change_list.append(change)
        
        """Third, extract the final list from all the sublists that were generated
         during the append process"""
        prof_loss_change_list=change_list[-1]

        """finally,find the average of all the items from the successive difference list"""
        avg_of_changes=np.mean(prof_loss_change_list)
    
        #The greatest increase in profits (amount) over the entire period
        for i in prof_loss_change_list:
            greatest_increase=max(prof_loss_change_list)
            
    
        #The greatest decrease in losses (amount) over the entire period
        for i in prof_loss_change_list:
            greatest_decrease=min(prof_loss_change_list)
            
        """to find the corresponding dates for greatest increase and greatest decrease
        values, create a dictionary from the successive difference list and dates then
        use print(dict.get(greatest_increase)) to find corresponding date"""
           
        """creating a list of dates from the date column of the csv file"""
        date_list.append(records[0])
        
        """removing Jan-2010 as that does not have a corresponding change"""
        change_date_list=date_list[1:total_months]
        
        """creating a dictionary to combine dates and corresponding change values"""
        changeDict={}
        for dates in change_date_list:
            for change in prof_loss_change_list:
                changeDict[dates]=change
                prof_loss_change_list.remove(change)
                break
        """source for changeDict code:
            https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/"""
            
        """reversing the key and value positions in the dictionary so I can pull date
        by max and min values"""
        reversed_change_dict = {}
        for key, value in changeDict.items():
           reversed_change_dict[value] = key
        """Source for code on reversing keys and values in dictionary:
             https://realpython.com/iterate-through-dictionary-python/#iterating-through-values"""
        
        """extracting corresponding dates for greatest increase and decrease from dictionary"""
        increase_date=reversed_change_dict.get(greatest_increase)
        decrease_date=reversed_change_dict.get(greatest_decrease)
        """source of code for dict.get()---python for everybody, chapter 9, page 110"""

    
    """Printing intermediary lists and dictionaries"""
    #print(f"profit loss change list: {change_list[-1]}")
    #print(f"date_list{date_list}")
    print("         ")
    print(f"change datelist: {change_date_list}")
    print("         ")
    print(f"changeDict: {changeDict}")
    print("         ")
    print("         ")
    
    
    """Printing results to terminal"""
    print(f"Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${netprofit:,d}")
    print(f"Average Change: ${avg_of_changes:,.2f}")
    print(f"Greatest Increase in Profits:{increase_date} (${greatest_increase:,d})")
    print(f"Greatest Decrease in Profits:{decrease_date} (${greatest_decrease:,d})")
   
    
#printing results to text file    
results_path=os.path.join("..","PyBank","Analysis","Financial_Analysis.txt")    
with open(results_path, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${netprofit:,d}\n")
    txtfile.write(f"Average Change: ${avg_of_changes:,.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase:,d})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease:,d})\n")
    

   
    



