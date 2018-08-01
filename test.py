# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:06:07 2018

@author: SANDEEP NITHYANANDAN
"""




import numpy as np
import re
import glob
from numpy import array
from numpy import genfromtxt
import nltk
import os
from numpy import genfromtxt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

y=[]
path="/home/sandeep/SANDEEP PROJECT/functional/cen/"
test_name=os.listdir(path)
test_name.sort()
#print(len(test_name))
count=0
for i in range(len(test_name)):# loop to set the class labels based on authors to variable y
    name=test_name[i]
    file_path=path+name+"/"
    count=count+1
    #print(file_path)
    file_len=(os.listdir(file_path))
    for j in range(len(file_len)):
        y.append(count)


y=array(y)
x=genfromtxt('train.csv',delimiter=',')#get the features to variable x from csv file




x_train, x_test,y_train, y_test = train_test_split(x, y, test_size = 1/3,random_state=42)#create train , test split
clf = MultinomialNB()#call the MutinomialNB
print("Started Training")
clf.fit(x_train,y_train)#fit the classifier
pred=clf.predict(x_test)#predict based on test set
print("acucracy is")
print((accuracy_score(y_test, pred)))#print accuracy
