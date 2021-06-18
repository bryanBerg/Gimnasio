from flask import Flask, jsonify, request
import requests


app=Flask(__name__)

@app.route('/membresia-controller/modification', methods=['PUT'])
def requestUpdate():
    data=request.get_json()
    fieldsRequired=["idmembresia","nombre","costo","areas"]
    if validateJson(data, fieldsRequired):
        #url="http://localhost:5010/membresia/modification" #LOCAL TEST
        url="http://membresia-model:5000/membresia/modification"
        response=requests.put(url, json=data)
        return response.json()
    else:
        return jsonify({"Message":"Verifique los parametros"})

def validateJson(json,fields) :
    if json is None:
        return False
    for field in fields:
        if field not in json:
            return False
    for field in fields:
        if json[field] is None or json[field] == "":
            return False
    return True

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)