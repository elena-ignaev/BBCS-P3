#all the imports for the ai part 

#First AI: Naive Bayes Classifer --------------------------------------------------------------

#SECOND AI: ----------------------------------------------------------------------------

#FLASK PART -------------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('homepage.html')

@app.route('/suggestions', methods=['GET', 'POST'])
def shown():
    return render_template('suggested.html')

# getting images from google maps api ------------------------------------------------------------
import googlemaps
import urllib.request

apikeyfile = open("apikey.txt", 'r')
apikey = apikeyfile.readline().strip() 
apikeyfile.close() 

# Initialize the Google Maps client with API key
gmaps = googlemaps.Client(key=apikey)

for i in range(1,4):
    # Get place details and retrieve photo reference
    place_name = "Sri Mariamman Temple" #replace with array[i-1]
    place_result = gmaps.places(query=place_name)
    photo_reference = place_result['results'][0]['photos'][0]['photo_reference']

    # Construct URL for photo
    photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key="+apikey

    path_name = 'static/locationpictures/img' + str(i)

    # Download photo from constructed URL
    urllib.request.urlretrieve(photo_url, path_name)
    # ---------------------------------------------------------------------------------------------

if __name__ == 'main':
    app.run(debug=True)

