from flask import Flask
from flask import render_template
import json
import requests

app = Flask(__name__)

def get_json():
    r = requests.get('https://www.offenesdatenportal.de/dataset/0cb093f5-3878-417d-88b5-8886cf47634a/resource/bc3f4e22-bd70-47ce-8603-9a1784b6b05c/download/geschichtsstation-1.json')
    data = r.json()
    return data

data_stationen = get_json()

@app.route("/")
def index():
    template='index.html'
    object_list = get_json()
    return render_template(template, object_list=object_list)

def zahl():
    zahl = 0
    for object in data_stationen['features']:
        object['properties']['ID'] = zahl
        zahl += 1
    return data_stationen
    
zahl_data = zahl()
# print(zahl_data)

def myid(): 
    for object in zahl_data['features']:
        return(object['properties']['ID'])

    
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = zahl()
    for row in data_stationen['features']:
        if row['properties']['ID'] == 3:
            return render_template(template, object=row)
    
if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
   
