# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:06:07 2018

@author: SANDEEP NITHYANANDAN
"""


import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
import re
import numpy as np
import os
import time
import csv
from numpy import genfromtxt
from nltk import word_tokenize
from nltk.tag import pos_tag


def functional_feature(content): #function to extract functional features
    text=word_tokenize(content)#tokenize the text to words
    tag_list=[]
    tag_write=[]
    tag_save=pos_tag(text)#save the POS tags 
    for i in range(len(tag_save)):
        tag_list.append(tag_save[i][1]) #append the POS tags to a list
    #print(tag_list)
    for i in range(55): # write the POS tag count to a tab separated file
        if i%2!=0:
            tag_write.append('\t')
        elif i==0:
            tag_write.append(tag_list.count('CC'))
        elif i==2:
            tag_write.append(tag_list.count('DT'))
        elif i==4:
            tag_write.append(tag_list.count('IN'))
        elif i==6:
            tag_write.append(tag_list.count('JJ'))
        elif i==8:
            tag_write.append(tag_list.count('JJR'))
        elif i==10:
            tag_write.append(tag_list.count('JJS'))
        elif i==12:
            tag_write.append(tag_list.count('NN'))
        elif i==14:
            tag_write.append(tag_list.count('NNS'))
        elif i==16:
            tag_write.append(tag_list.count('NNPS'))
        elif i==18:
            tag_write.append(tag_list.count('PDT'))
        elif i==20:
            tag_write.append(tag_list.count('POS'))
        elif i==22:
            tag_write.append(tag_list.count('PRP'))
        elif i==24:
            tag_write.append(tag_list.count('PRP$'))
        elif i==26:
            tag_write.append(tag_list.count('RB'))
        elif i==28:
            tag_write.append(tag_list.count('RBR'))
        elif i==30:
            tag_write.append(tag_list.count('RBS'))
        elif i==32:
            tag_write.append(tag_list.count('TO'))
        elif i==34:
            tag_write.append(tag_list.count('UH'))
        elif i==36:
            tag_write.append(tag_list.count('VB'))
        elif i==38:
            tag_write.append(tag_list.count('VBD'))
        elif i==40:
            tag_write.append(tag_list.count('VBG'))
        elif i==42:
            tag_write.append(tag_list.count('VBN'))
        elif i==44:
            tag_write.append(tag_list.count('VBP'))
        elif i==46:
            tag_write.append(tag_list.count('VBZ'))
        elif i==48:
            tag_write.append(tag_list.count('WDT'))
        elif i==50:
            tag_write.append(tag_list.count('WP'))
        elif i==52:
            tag_write.append(tag_list.count('WP$'))
        else:
            tag_write.append(tag_list.count('WRB'))
            
    for i in range(55):
        with open("file.txt","a") as fil:
            write_string=str(tag_write[i])
            fil.write(write_string)
            






char_leng=0
def write_file(data,count):
    with open("file.txt","a") as fil:
        data=str(data)
        if count==0:
            data=data+'\t'
            fil.write(data)
        else:
            fil.write(data)
            
        

def write_csv(): # create a csv file from the tab separated file
    txt_file=r"file.txt"
    csv_file=r"train.csv"
    in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t') #read from tab separated file
    out_csv = csv.writer(open(csv_file, 'w'))# write as csv
    out_csv.writerows(in_txt)
    




def struct(infile): # function to extract structural features
    f = open(infile, 'r')
    
    linecount = 0
    paragraphcount = 0
    empty = True
    for i in f:
        if '\n' in i:
            linecount += 1
            if len(i) < 2:
                empty = True
            elif len(i) > 2 and empty is True:
                paragraphcount = paragraphcount + 1
                empty = False
            if empty is True:
                paragraphnumber = 0
            else:
                paragraphnumber = paragraphcount
        
    f.close()
    write_file(paragraphcount,0)#save the paragraph count
    write_file(linecount,0)#save the line count
    
    #print("para count ",paragraphnumber,"line count ",linecount)
    with open(infile,"r")as fi:
        cont=fi.read()
    sentence=nltk.sent_tokenize(cont)
    word=nltk.word_tokenize(cont)
    #print("sentence ",len(leng))
    #print("word ",len(wo))
    write_file(len(sentence),0)
    write_file(len(word),0)
   # print("avg sen/para ",len(leng)/paragraphcount)
    #print("avg word/para",len(wo)/paragraphcount)
    #print("avg words/sen",len(wo)/len(leng))
    write_file(len(sentence)/paragraphcount,0)
    write_file(len(word)/paragraphcount,0)
    write_file(len(word)/len(sentence),1)
            





    
    





path="/home/sandeep/SANDEEP PROJECT/functional/cen/" # path to read the text of authors
test_name=os.listdir(path)# list the folder in the path

test_name.sort()#sort the folder alphabetically

count=0

for i in range(len(test_name)):
    name=test_name[i]
 
    file_path=path+name+"/"#get each text file path
    print(file_path)
    for filename in os.listdir(file_path):
        fil=file_path+filename
        print(fil)
        with open(fil) as file:#open each text
          
            
            content=file.read()
            struct(fil)
            functional_feature(content)
            
            with open("file.txt","a") as f:
                f.write("\n")
    
write_csv()


            

