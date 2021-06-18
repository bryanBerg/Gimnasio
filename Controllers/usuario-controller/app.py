from flask import Flask, jsonify, request
import requests

app=Flask(__name__)

@app.route('/usuario-controller/modification', methods=['PUT'])
def requestUpdate():
    data=request.get_json()
    fieldsRequired=["correousuario","telefono","nombre","apellidop","apellidom"]
    if validateJson(data, fieldsRequired):
        #url="http://localhost:5012/usuario/modification" #LOCAL TEST
        url="http://usuario-model:5000/usuario/modification"
        response1=requests.put(url, json=data)
        return response1.json()
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
    app.run(host="0.0.0.0", port=5002, debug=True)