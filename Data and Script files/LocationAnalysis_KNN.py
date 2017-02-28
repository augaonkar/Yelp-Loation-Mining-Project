# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 21:08:34 2016

@author: Abhilash Ugaonkar
"""

import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def loadData(fname):
    userBusinessVariables, labels = ([] for i in range(2))
    f=open(fname)
    for line in f:
        lists=[]
        listt=[]
        user,urating, business,brating, useful, userunique, alcohol, pricerange, noiselevel, businessunique, distance =line.strip().split(',')  			
        # variables for X and Y are:
        # X: userunique(uniquerumber), businessunique(uniquenumber), alcohol, noiselevel, pricerange
        # Y: binary 1/0 ex.[0,1,1,0,1]
        lists.append(userunique)
        lists.append(businessunique)
        lists.append(alcohol)
        lists.append(pricerange)
        lists.append(noiselevel)
        lists.append(distance)
        # userunique - Binary value is calculated based on user's previous rating - urating value.
        if float(urating) > 3 and int(useful) > 75:
            listt.append(1)
        else:
            listt.append(0)
        # businessunique - Binary value is calculated based on Business's overall rating - brating value.
        if float(brating) > 3:
            listt.append(1)
        else:
            listt.append(0)
        # alcohol value.
        if alcohol == '1':
            listt.append(1)	
        else:
            listt.append(0)
        # Pricerange value.
        if float(pricerange) == 2.5:
            listt.append(0) 
        else:
            listt.append(1)
        # Noise Level.
        if noiselevel == '1':
            listt.append(1)	
        else:
            listt.append(0)
            
        userBusinessVariables.append(lists)
        labels.append(listt)
    f.close()
    return userBusinessVariables,labels
	
	
#rev_train,labels_train=loadData('testFinal5.txt') #MinimaltrainingData
rev_train,labels_train=loadData('TrainingData.txt') #CompleteTrainingData
#rev_test,labels_test=loadData('testFinal6.txt') #testData
rev_test,labels_test=loadData('TestData.txt') #CompletetestData

#print (rev_test)
#print (labels_test)
 
neigh = KNeighborsClassifier(n_neighbors=3) #KNN value taken = 3
neigh.fit(rev_train, labels_train) 

#print(neigh.predict(rev_test))
print(neigh.predict_proba(rev_test))

#accuracy_score(labels_test, labels_test)
#accuracy_score(rev_test, labels_test)
#score(rev_test, labels_test, sample_weight=None)
#Build a counter based on the training dataset
#counter = CountVectorizer()
#counter.fit(rev_train)
#
#
##count the number of times each term appears in a document and transform each doc into a count vector
#counts_train = counter.transform(rev_train)#transform the training data
#counts_test = counter.transform(rev_test)#transform the testing data
#
##train classifier
#clf = MultinomialNB()
#
##train all classifier on the same datasets
#clf.fit(counts_train,labels_train)
#
##use hard voting to predict (majority voting)
#pred=clf.predict(counts_test)
#
##print accuracy
#print accuracy_score(pred,labels_test)
