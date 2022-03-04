from flask import Flask, request,jsonify      
import json 
from area import * 
from perimeter import * 
def data_receiver():  #receive data from postman body in json format
    data = request.get_json()           
    json_data = json.dumps(data)  
    obj = json.loads(json_data)                      
    return obj


app = Flask(__name__)
@app.route("/area", methods=["POST"]) 
def area_cal():    
    data=request.get_json()
    print("Data received via post: {}".format(data))
    # data = {"shape": "circle", "radius": 7}
    data_obj = g_data(data.get('shape'), data.get('radius'))
    obj_area = area(data_obj)
    if obj_area == -1:
        print("Error: Unrecognised shape.")
    print("area of object: {}".format(obj_area))
    response_data = {"area": obj_area}
    return json.dumps(response_data)


@app.route("/perimeter", methods=["POST"]) 
def perimeter_cal(): 
    data=data_receiver()
    print(data)
    cal_pm={"perimeter":" "}
    cal_pm["perimeter"]=perimeter(data) # function to calculate pm of geometric shapes imported from perimeter.py
    return jsonify(cal_pm)    

if __name__ == "__main__":              
    app.run()
