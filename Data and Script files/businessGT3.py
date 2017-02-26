import csv

with open('business.csv', 'r') as businessDataFile:
		count = 0
		businessReader = csv.reader(businessDataFile)
		businessfile  = open('businessGT3.csv', "w", newline='')
		writer = csv.writer(businessfile,delimiter=',', quoting = csv.QUOTE_ALL)
		#writer = csv.writer(user50file, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
		for business in businessReader:
			if business[3] != "" and business[3] is not None and float(business[3]) >= 2.5:
				writer.writerow(business)
		
		print ('Business Extracted!')			
		