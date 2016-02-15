from flask_frozen import Freezer
from app import app, zahl
freezer = Freezer(app)

@freezer.register_generator
def detail():
    object_list = zahl()
    for row in object_list['features']:
        row_id = 1
        yield {('row_id'): row['properties']['ID'] }
        row_id = row_id + 1 

if __name__ == '__main__':
    freezer.freeze()
    
