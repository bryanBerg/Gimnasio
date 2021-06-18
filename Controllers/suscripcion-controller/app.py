from flask import Flask, jsonify, request
import requests

app=Flask(__name__)

@app.route('/suscripcion-controller/modification', methods=['PUT'])
def requestUpdate():
    data=request.get_json()
    fieldsRequired=["idsuscripcion","idusuario","idmembresia","fechapago","fechaconclusion"]
    if validateJson(data, fieldsRequired):
        #url="http://localhost:5011/suscripcion/modification" #LOCAL TEST
        url="http://suscripcion-model:5000/suscripcion/modification"
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
    app.run(host="0.0.0.0", port=5001, debug=True)