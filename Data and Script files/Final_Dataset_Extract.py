#!/usr/bin/env python3
import csv
from math import sin, cos, radians, degrees, acos
from geopy.distance import vincenty

def calc_dist(lat_a, long_a, lat_b, long_b):
	pointA = (lat_a, long_a)
	pointB = (lat_b, long_b)
	return vincenty(pointA, pointB).miles
	#return degrees(acos(distance)) * 69.09


userDict={}
businessDict={}
userAvgStars={}
userVotesUseful={}
businessNoiseDict={}
businessPriceDict={}
businessAlcoholDict={}
	
#Users variables
with open('userGT50.csv', 'r') as userFile:
	userReader = csv.reader(userFile)
	uniqueNumber = 0
	for user in userReader:
		userAvgStars[user[3]]=user[2]
		userVotesUseful[user[3]]= user[0]
		if uniqueNumber not in userDict.values():
			if user[3] not in userDict:
				userDict[user[3]]=uniqueNumber
			uniqueNumber = uniqueNumber + 1
	print ('User Dictionaries ready!')							

#Business variables
with open('businessGT3.csv', 'r') as businessDataFile:
	businessReader = csv.reader(businessDataFile)
	uniqueNumber = 0
	for business in businessReader:            
		if(business[0] == 'average' or business[0] == 'quiet' or business[0] == ''):
			businessNoiseDict[business[7]]=1
		else:
			businessNoiseDict[business[7]]=0
		if(business[1] == ''):
			businessPriceDict[business[7]]=2.5
		else:
			businessPriceDict[business[7]]=business[1]
		if(business[6] == 'none' or business[6] == ''):
			businessAlcoholDict[business[7]]=1
		else:
			businessAlcoholDict[business[7]]=0    
		if uniqueNumber not in businessDict.values():
			if business[7] not in businessDict:
				businessDict[business[7]]=uniqueNumber
			uniqueNumber = uniqueNumber + 1
	print ('Business Dictionaries ready!')		
		
businessLat={}
businessLog={}
#Business location
with open('yelp_academic_dataset_businessLocationFields.csv', 'r') as businessDataFile:
		businessReader = csv.reader(businessDataFile)
		for business in businessReader:
				businessLat[business[3]]= business[0]
				businessLog[business[3]]= business[1]
		print ('Business Location Dictinory Ready!')		

userLat={}
userLog={}
#User location
with open('usersHomePlaceLatitudeandLongitude.csv', 'r') as userFile:
		userReader = csv.reader(userFile)
		for user in userReader:
				userLat[user[0]]= user[1]
				userLog[user[0]]= user[2]
		print ('User Location Dictinory Ready!')
		
userDicts = userAvgStars, userVotesUseful, userDict
businessDicts = businessNoiseDict, businessPriceDict,businessAlcoholDict, businessDict

with open('reviews.csv', 'r') as reviewsFile:
		reviewReader = csv.reader(reviewsFile)
		finalDatafile  = open('Extracted_Dataset.csv', "w", newline='')
		writer = csv.writer(finalDatafile,delimiter=',', quoting = csv.QUOTE_ALL)
		for review in reviewReader:
			if review[0] in userDict and review[2] in businessDict and review[0] in userLat:
				distance = calc_dist(float(businessLat[review[2]]), float(businessLog[review[2]]), float(userLat[review[0]]), float(userLog[review[0]]))
				writer.writerow(review + [d[review[0]] for d in userDicts] + [d[review[2]] for d in businessDicts] + [distance])
		print ('Final Data Extracted!')			
		