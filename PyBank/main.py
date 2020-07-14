import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

month = []
profit_total = []
diff_list = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        month.append(row[0])
        profit_total.append(int(row[1]))
    for r in range(len(profit_total)-1):
        diff_list.append(profit_total[r+1] - profit_total[r])
    greatest_increase = max(diff_list)
    greatest_decrease = min(diff_list)
    av_change = (sum(diff_list))/(len(month))

print("Financial Analysis")
print("-----------------------------------------------------")
print("The total number of months are ", len(month))
print(f"The total is ", sum(profit_total))
print(f"The average of the changes is ", {av_change})
print(f"The greatest increase was ", {greatest_increase})
print(f"The greatest decrease was ", {greatest_decrease})


txt_file =  os.path.join('Resources', 'PyBank results.txt')

with open('PyBank results.txt', 'w') as writer:
    f.write('Financial Analysis -----------------------------------------------------The total number of months are  86 The total is  38382578 The average of the changes is  {-196785} The greatest increase was  {1926159} The greatest decrease was  {-2196167}')

     














        

    








  


