# Authorship-Attribution

The project deals with identifying the author of a particular document which is given as input document. The system builds a model using Naive Bayes Classifier and based on the model performs the classification. The data set used is Corpus of English Novels(CEN).

It can be downloaded from https://perswww.kuleuven.be/~u0044428/cen.htm

Only 10 authors have been taken to classification. Any number of authors can be used.

Authur Conan Doyle          
Frances Burnett		    
Francis Marion Crawford	    
George Augustus Moore	    
George Gissing		    
Gilbert Parker		    
Henry Rider Haggard	    
Henry Seton Merriman	    
Kate Douglas Wiggin	    
Lyman Frank Baum	    

The project is implemented in Python 3. It uses the following:
NLTK
Sklearn
Pandas
NumPy

To use the project just change the directory where you have placed the dataset and run "mini_project_train.py"  to get 2 extra file , ie.

1) "file.txt" a tab spaced file created during feature extraction
2) "train.csv" the csv file used to train the system 
which is necessary for the exectuion.

Then run the file "test.py" to perform the prediction.

2 set  of features:

1)Functional 

2)Structural

are extracted.

A comparative study on which feature is essential for discriminating the author is also perfomed.
