# BBCS 2023 P3 Advanced Track Submission 
## Introduction 
### To be added 
## Idea 
### Create an Artificial Intelligence tool that references a database of destinations (only in Singapore in this project) and their features, and tries to find matches with user preferences (different from past travel activity). After that, the AI tool would generate sentences to explain its choices to the users, and suggest possible actions the user can take before travelling there. 
### Note to self: craft template sentences for the AI to output values for, since sentence construction is very difficult, while this is still AI. Also, the last part is 
## Details on AI Tool 
### The AI tools will have two parts. The first is a Naive Bayes Classifier, taking in user input as a query, lemmatizing the words and removing stop words as preprocessing, to decide good destinations to recommend to the user. The second part will be a series of transformers to generate a sentence to justify its recommendation to the user, with each run of it taking in a destinations as an output from the first part, as well as the words from user input after preprocessing in the first part. The second part will be run multiple times based on the results from the first part, to generate justifications for multiple recommendations for the users orderd based on preference by the first part. 
### Note to self: the descriptions will be generated based on what the users put in as well, not merely the destiantion. It's more based on input rather than destinations recommended. 
## Usage of the tool 
### To be added 
### Note to self: there will be multiple options generated for the users and it's generated for all. 
