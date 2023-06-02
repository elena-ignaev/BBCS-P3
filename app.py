#all the imports for the ai part 
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
import gensim
from gensim.models import word2vec
from sklearn.manifold import TSNE
#from sklearn.feature_extraction.text import TfidfVectorizer # if we're using word vectorization ig 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')

#First AI: Naive Bayes Classifer --------------------------------------------------------------

#loading stuff 

#for the lists later: no. of blanks is number of topics because yes. Each topic is assigned a certain "id". 
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
data = [[],[],[],[],[],[],[],[],[],[],[]]
freqs = [[],[],[],[],[],[],[],[],[],[],[]]
topiclookup = ['comarchitecture', 'algs', 'flowcharts', 'python', 'validation', 'safeuse', 'numbersystems', 'logiccircuits', 'spreadsheets', 'networks', "spam"] #index of occurrence of topic name in list is the topic "id"
chances = [1 for i in range(len(topiclookup))]

#reading machine learning data into the lists "data" and "freqs", also I just gave up and made weird variable names
fd = open("TAMLdata.txt", 'r')
ff = open("TAMLfreqs.txt", 'r')
for x in range(len(data)):
    data[x] = fd.readline().split()
    freqs[x] = list(map(int, ff.readline().split())) #this is just a way to read the values into a list but make them all int.
print(data)
print(freqs)

def filtertext(): 
    # input the text
    text = input("Text: ")
    word_tokenize(text)

    tokens = word_tokenize(text)
    
    # initiate the lemmatizer object
    lemmatizer = WordNetLemmatizer()

    new_tokens = [] 
    for token in tokens: 
        new_tokens.append(lemmatizer.lemmatize(token))
    #print(new_tokens)
    
    #assign to globally set stopwords to a local set
    stop_words = set(stopwords.words('english')+[''])
    #filter the stopwords and non-alphanumeric characters from the token
    filtered_tokens = [''.join(ch for ch in token if ch in letters) for token in new_tokens if not ''.join(ch for ch in token if ch in letters).lower() in stop_words]

    return filtered_tokens

def test():
    for i in t:
        for a in range(len(topiclookup)): 
            if i in data[a]:
                chances[a] *= (freqs[a][data[a].index(i)]+1)/(sum(freqs[a]))
            else:
                chances[a] *= 1/(sum(freqs[a]))
    return topiclookup[chances.index(max(chances))]


#SECOND AI: ----------------------------------------------------------------------------



#FLASK PART -------------------------------------------
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

cur_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(cur_dir, 'bulletin.db')
app = Flask(__name__)
os.path.join(cur_dir, "TAMLfreqs.txt")
os.path.join(cur_dir, "TAMLdata.txt")

## in case db is locked, run this
# db = sqlite3.connect(db_file) 
# db.close()

if __name__ == '__main__':
    app.run(debug=True) 
    # set debug to False if you are using python IDLE as 
    # your IDE.

