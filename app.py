#all the imports for the ai part 

#First AI: Naive Bayes Classifer --------------------------------------------------------------

#SECOND AI: ----------------------------------------------------------------------------

#FLASK PART -------------------------------------------
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('homepage.html')

@app.route('/suggestions', methods=['GET', 'POST'])
def shown():
    # getting images from google maps api ------------------------------------------------------------
    import googlemaps
    import urllib.request
    apikeyfile = open("apikey.txt", 'r')
    apikey = apikeyfile.readline().strip() 
    apikeyfile.close() 

    # Initialize the Google Maps client with API key
    gmaps = googlemaps.Client(key=apikey)

    # Get place details and retrieve photo reference
    place_name = "Sri Mariamman Temple" #replace with array[i-1]
    place_result = gmaps.places(query=place_name)
    photo_reference = place_result['results'][0]['photos'][0]['photo_reference']
    # Construct URL for photo
    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={apikey}"
    # Get image
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], photo_url)
    
    # Get place details and retrieve photo reference
    place_name = "Sri Mariamman Temple" #replace with array[i-1]
    place_result = gmaps.places(query=place_name)
    photo_reference = place_result['results'][0]['photos'][0]['photo_reference']
    # Construct URL for photo
    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={apikey}"
    # Get image
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], photo_url)

    # Get place details and retrieve photo reference
    place_name = "Sri Mariamman Temple" #replace with array[i-1]
    place_result = gmaps.places(query=place_name)
    photo_reference = place_result['results'][0]['photos'][0]['photo_reference']
    # Construct URL for photo
    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={apikey}"
    # Get image
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], photo_url)
    
    return render_template('suggested.html', pic1=img1, pic2=img2, pic3=img3)
    # ---------------------------------------------------------------------------------------------

if __name__ == 'main':
    app.run(debug=True)