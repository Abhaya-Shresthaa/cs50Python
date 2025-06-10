import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit() #terminate the whole program
    
requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

print(json.dumps(response.json(), indent= 2)) #indent means spacing with 2

demo = response.json()
for result in demo["results"]:
    print(result["trackName"])