 import csv
>>> with open('crime.csv', 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in reader:
         print ', '.join(row)

