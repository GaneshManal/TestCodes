from flask import Flask, request
import json
from shape import Circle, Square


app = Flask(__name__)
@app.route("/area", methods=["POST"]) 
def calculate_area():    
    data=request.get_json()
    shape_obj = None
    if data.get('shape').lower() == "circle":
        shape_obj = Circle(data.get('radius'))
    if data.get('shape').lower() == "square":
        shape_obj = Square(data.get('radius'))

    area = shape_obj.get_area()
    print("area of object: {}".format(area))
    response_data = {"area": area}
    return json.dumps(response_data)

@app.route("/perimeter", methods=["POST"]) 
def perimeter_cal(): 
    data=request.get_json()
    shape_obj = None
    if data.get('shape').lower() == "circle":
        shape_obj = Circle(data.get('radius'))
    if data.get('shape').lower() == "square":
        shape_obj = Square(data.get('radius'))

    perimeter = shape_obj.get_perimeter()
    print("perimeter of object: {}".format(perimeter))
    response_data = {"perimeter": perimeter}
    return json.dumps(response_data)
if __name__ == "__main__":              
    app.run()
