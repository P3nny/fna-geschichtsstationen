import urllib, json
url = "https://www.offenesdatenportal.de/dataset/0cb093f5-3878-417d-88b5-8886cf47634a/resource/bc3f4e22-bd70-47ce-8603-9a1784b6b05c/download/geschichtsstation-1.json"
print(url)
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
