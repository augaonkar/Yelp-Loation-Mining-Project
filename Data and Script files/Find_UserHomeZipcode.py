import csv
import operator;

userDict={}
businessDict={}
businessZipDict={}
userZipListDict={}
#UsersId
with open('userGT50.csv', 'r') as userFile:
		userReader = csv.reader(userFile)
		for user in userReader:
			userDict[user[3]]=userDict.get(user[3],0)+1;
		print ('Users Dictinory Ready!')
		
#Business Id
with open('businessGT3.csv', 'r') as businessDataFile:
		businessReader = csv.reader(businessDataFile)
		for business in businessReader:
			businessDict[business[7]]=businessDict.get(business[7],0)+1;
		print ('Business Dictinary Ready!')		

#BusinessZip Id
with open('yelp_academic_dataset_businessLocationFields.csv', 'r') as businessDataFile:
		businessReader = csv.reader(businessDataFile)
		for business in businessReader:
			if business[3] in businessDict:
				businessZipDict[business[3]]=business[2][-5:];
		#print(businessZipDict)
		print ('Business Zip Dictinary Ready!')			

with open('reviews.csv', 'r') as reviewsFile:
		reviewReader = csv.reader(reviewsFile)
		#print (userDict)
		#print (businessDict)
		for review in reviewReader:
			if review[0] in userDict and review[2] in businessDict:
				#if review[0] not in userZipListDict:
				userZipListDict.setdefault(review[0], []).append(businessZipDict[review[2]])
				#elif review[0] in userZipListDict:
				#userZipListDict[review[0]] = userZipListDict[review[0]].append(businessZipDict[review[2]])
				#writer.writerow(review + [d[review[0]] for d in userDicts] + [d[review[2]] for d in businessDicts])
				#writer.writerow(review + userAvgStars[review[0]] + userVotesUseful[review[0]])
		#print (userZipListDict)		
		print ('Final Data Extracted!')			

# returns the zipcode with atleast 60% attendence.
def findHomeZip(userZipList):
	zipDict={}
	try:
	#	print ('Heello')
	#	print (userZipList)
		for zip in userZipList:
	#		print (zip)
			zipDict[int(zip)] = zipDict.get(int(zip),0)+1
		topZip = getTop1(zipDict)
		return topZip
	except ValueError:
		return 0
		#break
		
def getTop1(D):
	result=[]
	homeZip = 0
	#print (D)
	SortbyValue=sorted(D.items(),key=operator.itemgetter(1),reverse=True)
	#print (SortbyValue)
	SortbyValue=SortbyValue[0:1]
	#print(SortbyValue)
	for word in SortbyValue:
		#print (word)
		result.append(word[1])
		result.append(word[0])
		#print (result[0])
		#print (len(D)/2)
	#print (result[1])
	if result[0] > (len(D)/2):
		return result[1]
	else:
		return 0
	#return SortbyValue
	
userHomeZip={}
#finalDatafile  = open('UserHomeZip.csv', "w", newline='')
#writer = csv.writer(finalDatafile,delimiter=',', quoting = csv.QUOTE_ALL)
for key in userZipListDict:
		zip = findHomeZip(userZipListDict[key])
		if zip != 0:
			userHomeZip[key] = zip
			#writer.writerow([key]+[userHomeZip[key]])
print ('UserHomeZip Successful')		


businessLatitude={}
businessLongitude={}
#Business LAtitute and longitude - column 2 and column 5
with open('businessGT3.csv', 'r') as businessDataFile:
		businessReader = csv.reader(businessDataFile)
		for business in businessReader:
			businessLatitude[business[7]] = business[2]
			businessLongitude[business[7]] = business[5]
		print ('Latitude and Longitude!')

usersHomePlaceLatitude={}
usersHomePlaceLongitude={}
print(businessZipDict)
print(userHomeZip)

finalDatafile  = open('usersHomePlaceLatitudeandLongitude.csv', "w", newline='')
writer = csv.writer(finalDatafile,delimiter=',', quoting = csv.QUOTE_ALL)
for key in businessZipDict:
	for userKey in userHomeZip:
		if businessZipDict[key] == str(userHomeZip[userKey]) and userKey not in usersHomePlaceLatitude:
			usersHomePlaceLatitude[userKey] = businessLatitude[key]
			usersHomePlaceLongitude[userKey] = businessLongitude[key]
			writer.writerow([userKey]+[usersHomePlaceLatitude[userKey]]+[usersHomePlaceLongitude[userKey]])
print ('User Latitude and Longitude!')	
			
		