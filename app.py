
from flask import Flask
from flask import render_template
from flask import abort
import json
import requests

app = Flask(__name__)

def get_json():
    r = requests.get('https://www.offenesdatenportal.de/dataset/0cb093f5-3878-417d-88b5-8886cf47634a/resource/bc3f4e22-bd70-47ce-8603-9a1784b6b05c/download/geschichtsstation-1.json')
    data = r.json()
    return data

data_stationen = get_json()

def zahl():
    zahl = 1
    data_stationen = get_json()
    for object in data_stationen['features']:
        object['properties']['ID'] = zahl
        object['geometry']['x'] = object['geometry']['coordinates'][:1]
        object['geometry']['y'] = object['geometry']['coordinates'][1:]
        zahl += 1
    return data_stationen
    
zahl_data = zahl()

def myid(): 
    for object in zahl_data['features']:
        return(object['properties']['ID'])

@app.route("/")
def index():
    template='index.html'
    object_list = zahl()
    return render_template(template, object_list=object_list)

    
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = zahl()
    for row in object_list['features']:
        if row['properties']['ID'] == int(row_id):
            return render_template(template, object=row, object_list=object_list)
    abort(404)
    
if __name__=='__main__':
    app.run(debug=True, use_reloader=True)
   
