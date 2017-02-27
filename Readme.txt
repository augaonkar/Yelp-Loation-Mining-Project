Instructions:	
	
1. 'TrainingData.txt' consists of Training data.
2. 'TestData.txt' consists of Test Data.
3.  LocationAnalysis_KNN.py contains the KNNClassifier analysis with training and test data as input.
	This needs to be executed in anaconda python 2.7 using spyder application if possible.
4. Execute the knn analysis file without including the disctance parameter and then include it, compare the results as shown in the video.
Note: 'Final_Dataset_Extract' is copied into Dataset_Complete.csv and open in notepad to save as TrainingData. Then we take a sample for the TestData.txt from this data.
	
	
	Below steps are the initial steps to get the final data in step1. This is just for the reference. 
	If trying to execute the scripts, use python 3.5
Initial extraction of csv files using json files - python commands:
	- python BUSINESS_json_to_csv_converter.py yelp_academic_dataset_business.json
	- python BUSINESS_Zipcode_json_to_csv_converter12.1.16.py yelp_academic_dataset_business.json
	- python REVIEWS_json_to_csv_converter.py yelp_academic_dataset_review.json, change the output file name to reviews.csv
	- python USER_json_to_csv_converter.py yelp_academic_dataset_user.json
	
The Main dataset has been created using 'Final_Dataset_Extract.py' script file.
	Inputs needed for this file are:
	i.  userGT50.csv - users with review count > 50
	ii. businessGT3.csv - businesses with average review > 2.5
	iii.yelp_academic_dataset_businessLocationFields.csv - business data along with zipcode, latitude and longitude values.
	iv. usersHomePlaceLatitudeandLongitude,csv - users derived latitude and longitude data.
	v.  reviews.csv - reviews dataset
Script files used to create the above files included in above step (In same order as given)
	- businessGT3.py, generates userGT50.csv
	- usersGT50.py, generates businessGT3.csv
	- Find_UserHomeZipcode.py, This creates usersHomePlaceLatitudeandLongitude.csv file.
	

