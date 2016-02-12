import json
import pandas as pd
import requests

# Pull down some simple json data
r = requests.get('https://www.offenesdatenportal.de/dataset/0cb093f5-3878-417d-88b5-8886cf47634a/resource/bc3f4e22-bd70-47ce-8603-9a1784b6b05c/download/geschichtsstation-1.json')

# Convert it into a python object
data = r.json()

print(data)
