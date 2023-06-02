import googlemaps
import urllib.request

# Step 1: Install the googlemaps library by running 'pip install googlemaps'

# Step 2: Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyDBXoA4A2VKNeibxkDJayt9TvypZaUmnMk')

# Step 3: Get the place details and retrieve the photo reference
place_name = "Sri Mariamman Temple"
place_result = gmaps.places(query=place_name)
photo_reference = place_result['results'][0]['photos'][0]['photo_reference']

# Step 4: Construct the URL for the photo
photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key=AIzaSyDBXoA4A2VKNeibxkDJayt9TvypZaUmnMk"

# Step 5: Download the photo from the constructed URL
urllib.request.urlretrieve(photo_url, 'location_photo.jpg')
print("Photo downloaded successfully!")
