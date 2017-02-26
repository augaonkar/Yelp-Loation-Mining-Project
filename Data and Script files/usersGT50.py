import csv

with open('users.csv', 'r') as userFile:
		count = 0
		userReader = csv.reader(userFile)
		user50file  = open('userGT50.csv', "w", newline='')
		writer = csv.writer(user50file,delimiter=',', quoting = csv.QUOTE_ALL)
		#writer = csv.writer(user50file, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
		for user in userReader:
			if user[1] != "" and user[1] is not None and float(user[1]) > 50:
				writer.writerow(user)
		
		print ('Users Extracted!')			
		