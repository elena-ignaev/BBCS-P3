# BBCS 2023 P3 Advanced Track Submission 
## Introduction 
### In the travel industry, often, Artificial Intelligence Tools recommending destinations for travel seem to either consider past travel activity from users (which is counterproductive since users may prefer going to many new places or going to similar places, unpredictable by the AI), or are mostly merely showing descriptions of any recommended destinations, not being very personalized for the user. This is not ideal, since 
## Idea 
### Create an Artificial Intelligence tool that references a database of destinations (only places in Singapore in this project) and their features, and tries to find matches with user preferences (different from past travel activity, considering that users could want to visit new places; in this case, user input). The AI would first generate 3 top suggestions for possible destinations, then the AI tool would generate sentences to explain its choices to the users and give details about the destinations. 
## Details on AI Tool 
### The AI tool will have two parts. The first is a Naive Bayes Classifier, taking in user input as a query, lemmatizing the words and removing stop words as preprocessing, to decide good destinations to recommend to the user. The second part will be a series of transformers to generate a sentence to justify its recommendation to the user, with each run of it taking in a destinations as an output from the first part, as well as the words from user input after preprocessing in the first part. The second part will be run multiple times based on the results from the first part, to generate justifications for multiple recommendations for the users orderd based on preference by the first part. 
### An important note is that the descriptions will be generated based on what the users put in as well, not merely the destiantion, and it is planned to be more based on input rather than destinations recommended, to increase personalization and make it (hopefully) better than merely showing a fixed description each destination. 
## Usage of the tool 
### At the homepage (picture below), you will type in a search query into the search bar, and it will redirect you to the search page. 
### ![Image of homepage of website](/prototyping/homepage.jpeg) 
### The following is an image of the search page: 
### ![Image of search page of website](/prototyping/searchpage.jpeg) 
## Ending words 
### We hope that this project is helpful for the travel industry, and will turn out useful for users. 
