import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
		csvreader = csv.reader(csvfile)

		csv_header = next(csvreader)
		
		counter = 0


		for row in csvreader:
			counter += 1

		



		print('Total Votes: ' + str(counter))