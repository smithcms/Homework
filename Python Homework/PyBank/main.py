import os
import csv
import numpy as np
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile)

	csv_header = next(csvreader)
	line1 = next(csvreader)
	counter = 1
	total_number = int(line1[1])
	(csv_header[0])
	previous_data = int(line1[1])
	changes = []
	months = []
	for row in csvreader:
		if counter != 0:
			changes.append(int(row[1]) - int(previous_data))
			months.append(row[0])
			previous_data = int(row[1]) 

			
		counter += 1
		total_number = int(row[1]) + total_number
	dictionary = dict(zip(changes, months))
	(dictionary.get(np.max(changes)))
	(dictionary.get(np.min(changes)))

	print('FINANCIAL ANALYSIS')
	print('-----------------------------')
	print('Total Months: ' + str(counter))
	print('Total: $' + str(total_number))
	print('Average Change: $' + str(round(np.mean(changes), 2)))
	print('Greatest Increase in Profits: ' + str(dictionary.get(np.max(changes))) + ' ($' + str(np.max(changes)) + ')')
	print('Greatest Decrease in Profits: ' + str(dictionary.get(np.min(changes))) + ' ($' + str(np.min(changes)) + ')')