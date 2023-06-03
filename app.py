if __name__ == "__main__": 

    #all the imports for the ai part 

    print("Importing modules... ") 
    import pandas as pd 
    pd.options.mode.chained_assignment = None
    import numpy as np
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('omw-1.4')
    nltk.download('wordnet')
    #import gensim
    #from gensim.models import Word2Vec
    from gensim.models import KeyedVectors 
    #from sklearn.manifold import TSNE
    #from sklearn.feature_extraction.text import TfidfVectorizer # if we're using word vectorization ig 
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import stopwords

    #First AI: Naive Bayes Classifer --------------------------------------------------------------

    print("LOADING FIRST AI - Naive Bayes Classifier")

    #loading stuff

    #initialize lemmatizer
    print("Initializing lemmatizer and related functions... ") 
    lemmatizer = WordNetLemmatizer()

    #define filter text function using lemmatizer 
    def filtertext(text): 
        new_tokens = [] 
        for token in word_tokenize(text): 
            new_tokens.append(lemmatizer.lemmatize(token))
        
        #assign to globally set stopwords to a local set
        stop_words = set(stopwords.words('english')+[''])
        
        #filter the stopwords and non-alphanumeric characters from the token
        filtered_tokens = [''.join(ch for ch in token if ch in letters) for token in new_tokens if not ''.join(ch for ch in token if ch in letters).lower() in stop_words]

        return filtered_tokens 

        '''
        #the following seems to be code for vectorization as well 
        #vectorizer = TfidfVectorizer()
        #vectorizer.fit()
        #print(vectorizer.vocabulary_)
        #print(vectorizer.idf_)
        vectors = vectorizer.transform(filtered_tokens)
        #print(vectors.shape)
        #print(vectors.toarray())
        return vectors.toarray() #returns word vectors '''

    #for the lists later: no. of blanks is number of topics because yes. Each topic is assigned a certain "id". 
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #read in location data
    print("Loading locations... ") 
    fl = open("LocationData.csv", 'r') #will be formatted such that odd lines are location names and evens are tags 
    rawLocs = fl.readlines()
    fl.close()

    #Load locations and corresponding tags 
    locTags = {}
    values = [] 
    for x in range(1, len(rawLocs)-2):
        temp = rawLocs[x].split(',')
        temp2 = [] 
        for i in range(1, len(temp)):
            temp2 += filtertext(temp[i].strip()) 
        locTags[temp[0]] = temp2
        values += temp2 

    #compile list of tags 
    #values = locTags.values()
    taglookup = []
    for i in values:
        taglookup.append(i) 
    taglookup = list(set(taglookup))
    #print("Taglookup:", taglookup) 

    #Load pre-trained Word2Vec model
    print("Loading vectorizer... (This is usually the longest step)") 
    vectorizer = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    # Calculate the vector representation for the keywords
    print("Loading vectors... ") 
    keyword_vectors = []
    i = 0 
    while i < len(taglookup):
        try:
            temp = vectorizer[taglookup[i]]
        except Exception as ex:
            name = str(ex).split("'")[1]
            taglookup.remove(name)
            continue
        keyword_vectors.append(temp) 
        i += 1 
    #keyword_vectors = [vectorizer[word] for word in taglookup]


    #print(locTags)
    print("Loading complete!") 

    #define function to get word similarities 
    def word_similarities(target_word): 
        words = [word for word in taglookup] 
        distances = vectorizer.distances(target_word, words) #ordered based on orders of vocabulary it seems
        return (distances-np.min(distances))/(np.max(distances)-np.min(distances))

    #function to test this 
    def gettopthree(text):
        global training
        global data
        global freqs
        t = filtertext(text)
        chances = [1 for i in range(len(locTags))]
        #print(t)
        for inword in t:
            try:
                scores = word_similarities(inword)
                #print(inword)
                #print(scores) 
                i = 0 
                for tags in locTags.values():
                    c = 1 #chance
                    for tag in tags:
                        try: 
                            c *= (1-scores[taglookup.index(tag)])*0.8 + 0.2 #to make sure it doesnt go to like 0
                        except:
                            pass 
                    chances[i] *= c
                    i += 1 
            except Exception as ex:
                '''for i in range(len(chances)): 
                    chances[i] /= 20 #punishment for not matching'''
                #actl if it punishes all equally then nothing impt 
                print(ex)
        #return chances
        s = sorted(chances)
        #print(chances)
        #print(s[-10:])
        #return list(locTags.keys())[chances.index(max(chances))]
        locations = list(locTags.keys())
        res = []
        i = 0 
        while i < 3:
            indices = []
            for idx, value in enumerate(chances):
                if value == s[-1-i]:
                    indices.append(idx)
            while i < 3 and len(indices) > 0:
                res.append(list(locTags.keys())[indices[-1]])
                indices.pop()
                i += 1 
        return res 

    #SECOND AI: ----------------------------------------------------------------------------


def generateDesc(user_input, destination): 
    text = ""; # replace with ai; user input will be user input text, destination is destination name 
    return text 



#FLASK PART ------------------------------------------------------------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request 
#import os
#import requests 
#import googlemaps
import pandas as pd
#import urllib.request

df = pd.read_csv("LocationData.csv", header=None)

def get_image_location(name):
    for index in range(0, 245):
        print(df[0][index])
        print(name)
        print(df[0][index] == name)
        if df[0][index] == name:
            image_index = index + 1
            image_url = "static/locationpictures/img" + str(image_index) + ".jpg"
            return image_url
    return None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('homepage.html')

@app.route('/suggestions', methods=['GET', 'POST'])
def shown():
    
    #apikeyfile = open("apikey.txt", 'r')
    #apikey = apikeyfile.readline().strip() 
    #apikeyfile.close() 

    # Initialize the Google Maps client with API key
    #gmaps = googlemaps.Client(key=apikey)

    if not ('query' in request.args): 
        return "Enter query", 400 
    
    query = request.args.get('query')
    array = gettopthree(query)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    df = pd.read_csv("LocationData.csv")

    img1 = get_image_location(array[0])
    img2 = get_image_location(array[1])
    img3 = get_image_location(array[2])

    #do stuff with second AI here ------------------------------------------------------------------------------------------------
    
    txt1 = generateDesc(query, array[0]) 
    txt2 = generateDesc(query, array[1]) 
    txt3 = generateDesc(query, array[2]) 
    print(img1)
    return render_template('suggested.html', searchquery=query, pic1=img1, pic2=img2, pic3=img3, loc1=array[0], loc2=array[1], loc3=array[2], desc1=txt1, desc2=txt2, desc3=txt3)
    # ---------------------------------------------------------------------------------------------

if __name__ == "__main__": 
    app.run(debug=True)