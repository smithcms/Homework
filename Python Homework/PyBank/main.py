import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile)

	csv_header = next(csvreader)
	counter = 0
	total_number = 0
	for row in csvreader:
		counter += 1
		total_number = int(row[1]) + total_number
	print(counter)
	print(total_number)

