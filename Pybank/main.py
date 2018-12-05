import os
import csv
csvpath = os.path.join('budget_data.csv')
file_output=os.path.join('output_file.txt')
total_rev=0
total_months=0
month_of_change = []
change_list = []
increase = ["", 0]
decrease = ["", 99999999]
prev_rev =0

#with open(csvpath, 'r') as file_handler:
#    lines=file_handler.read()
 #   print (lines)
  #  print(type(lines))
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    csv_header=next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_rev=total_rev + int(row[1])
        total_months=total_months + 1
        r_change = int(row[1]) - prev_rev
        prev_rev = int(row[1])
        change_list = change_list + [r_change]
        month_of_change = month_of_change + [row[0]]
        if (r_change > increase[1]):
            increase[0] = row[0]
            increase[1] = r_change

        if (r_change < decrease[1]):
            decrease[0] = row[0]
            decrease[1] = r_change
    ch_avg = sum(change_list) / len(change_list)

    print ("Financial Analysis")
    print ("_____________________")
    print ("Total Months:  " + str(total_months))
    print ("Total Amount:  " + str(total_rev))
    print ("Average Change: " + str(ch_avg))
    print ("Greatest Increase in Profits" + str(increase))
    print ("Greatest Decrease in Profits" + str(decrease))
    
    with open(file_output, "w") as txt_file:
        txt_file.write("Total Months:  " + str(total_months))
        txt_file.write("Total Amount:  " + str(total_rev))
        txt_file.write("Average Change: " + str(ch_avg))
        txt_file.write("Greatest Increase in Profits" + str(increase))
        txt_file.write("Greatest Decrease in Profits" + str(decrease))

