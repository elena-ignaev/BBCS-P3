import urllib.request
from gmaps_static import GoogleMapsStatic

# Step 1: Install the gmaps-static library by running 'pip install gmaps-static'

# Step 2: Initialize the GoogleMapsStatic client with your API key
gmaps = GoogleMapsStatic(api_key='YOUR_API_KEY')

# Step 3: Get the static map image of the location
location_name = 'Marina Bay Sands'
map_url = gmaps.generate_map(location_name, size=(600, 400), zoom=13)

# Step 4: Download the image from the constructed URL
urllib.request.urlretrieve(map_url, 'location_map.png')
print("Image downloaded successfully!")
