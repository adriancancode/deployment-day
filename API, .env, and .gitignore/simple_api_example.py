# create a virtual environment! 
# \venv\Scripts\activate  
# source venv/bin/activate
#
# Install the necessary packages!
# run this -> pip install -r requirements.txt
import requests
from dotenv import load_dotenv
import os

# Looks for .env file
load_dotenv()

# 1. Set your API key as a variable SAFELY
api_key = os.getenv("UNSPLASH_ACCESS_KEY")
ENDPOINT = "https://api.unsplash.com/search/photos"

# 2. Set up the Search Parameters
# This tells the API exactly what we are looking for
search_parameters = {
    "query": "cyberpunk",  # The word we are searching for
    "per_page": 3,         # How many results we want back (max is 30)
    "orientation": "landscape" # Optional: landscape, portrait, or squarish
}

# 3. Set up the Headers for Authentication
# Unsplash wants the key passed securely in the HTTP Header, not the URL
headers = {
    "Authorization": f"Client-ID {api_key}"
}

print(f"Searching Unsplash for '{search_parameters['query']}' photos...\n")

try:
    # 4. Make the GET request to the API
    response = requests.get(ENDPOINT, params=search_parameters, headers=headers)
    
    # 5. Check if the request was successful (Status Code 200)
    response.raise_for_status() 
    
    # 6. Convert the response data into a Python Dictionary (JSON)
    data = response.json()
    
    # 7. Loop through the results and print the image URLs
    results = data.get("results", [])
    
    if not results:
        print("No images found for that search!")
    else:
        for index, photo in enumerate(results):
            image_url = photo["urls"]["regular"]
            photographer = photo["user"]["name"]
            
            print(f"Photo {index + 1} by {photographer}:")
            print(f"{image_url}\n")

except requests.exceptions.HTTPError as err:
    # This will catch errors like a 401 Unauthorized (wrong API key) 
    # or a 403 Forbidden (rate limit exceeded)
    print(f"HTTP Error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")