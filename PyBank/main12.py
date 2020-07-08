import os
import csv
#path = os.path.join("Resources", "budget_data.csv")
path = os.path.join('Resources', 'budget_data.csv')

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the headers
    monthsum = 0      #establish variables
    Total_Profit = 0
    maxInc = 0
    maxDec = 0    
    Change1 = []      #establish lists
    Change2 = []
    data = []
    data2 = [] 
    MaxInc_p = 0
    MaxDec_p = 0

    for row in csv_reader:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        monthsum += 1
        Total_Profit = int(row[1]) + int(Total_Profit)    
        Change1.append(int(row[1]))  #Adds the profit/loss for earch month to a list
        data.append(row[0])
        
    for i in range(len(Change1)-1):
        Change2.append(Change1[i + 1] - Change1[i])  #Adds the differences between two months to a list
        if Change1[i + 1] - Change1[i] > maxInc:
            maxInc = Change1[i + 1] - Change1[i]
            MaxInc_p = i + 1
        if Change1[i + 1] - Change1[i] < maxDec:
            maxDec = Change1[i + 1] - Change1[i]
            MaxDec_p = i + 1
    TmaxInc = (data[MaxInc_p])
    TmaxDec = (data[MaxDec_p])
    
    AveChange = (sum(Change2) / len(Change2))
    AveChange = ("{:.2f}".format(AveChange))

    print (' ')  #output
    print ('          Financial Analysis')  
    print ("----------------------------------------") 
    print ('Total Months:  ' + str(monthsum))
    print ('Total:   $' + str(Total_Profit))
    print ('Average Change:   $' + str(AveChange))   
    print ('Greatest Increase in Profits:   ' + TmaxInc +' ($' + str(maxInc) + ')')
    print ('Greatest Decrease in Profits:   ' + TmaxDec +' ($' + str(maxDec) + ')')
    print (" ")
    
    # Print the contents of the text file
output_path = os.path.join('Analysis', 'PyBankResults.txt')

output_path = open(output_path, 'w+')

output_path.write('\n          Financial Analysis')
output_path.write('\n----------------------------------------')
output_path.write('\nTotal Months:  ' + str(monthsum))
output_path.write('\nTotal:   $' + str(Total_Profit))
output_path.write('\nAverage Change:   $' + str(AveChange))
output_path.write('\nGreatest Increase in Profits:   ' + TmaxInc +' ($' + str(maxInc) + ')')
output_path.write('\nGreatest Decrease in Profits:   ' + TmaxDec +' ($' + str(maxDec) + ')')
output_path.close() 
