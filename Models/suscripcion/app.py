from flask import Flask, jsonify, request
import psycopg2

app=Flask(__name__)

PSQL_HOST = "gym-db" #"localhost"
PSQL_USER = "admin"
PSQL_PASS = "esime2021"
PSQL_DB   = "gym_database"

@app.route('/suscripcion/modification', methods=['PUT'])
def ModificarSuscripcion():
    try:
        conection=psycopg2.connect(host=PSQL_HOST, database=PSQL_DB, user=PSQL_USER, password=PSQL_PASS)
        cur=conection.cursor()
        data=request.get_json()
        query="select * from membresia where idmembresia=%s;"
        cur.execute(query,(data["idmembresia"],))
        membresia=cur.fetchone()
        query="select * from usuario where correousuario=%s;"
        cur.execute(query,(data["idusuario"],))
        usuario=cur.fetchone()
        query="select * from suscripcion where idsuscripcion=%s;"
        cur.execute(query,(data["idsuscripcion"],))
        suscripcion=cur.fetchone()
        if membresia and usuario and suscripcion:
            query=f"update suscripcion set idusuario='{data['idusuario']}', idmembresia={int(data['idmembresia'])}, fechapago='{data['fechapago']}', fechaconclusion='{data['fechaconclusion']}' where idsuscripcion={int(data['idsuscripcion'])}"
            cur.execute(query)
            conection.commit()
            cur.close()
            conection.close()
            return jsonify({"Message":"Modificado con exito"}),200
        elif suscripcion==None:
            return jsonify({"Message":"la suscripcion no existe"}),404
        elif usuario==None:
            return jsonify({"Message":"el usuario no existe"}),404
        elif membresia==None:
            return jsonify({"Message":"la membresia no existe"}),404
    except psycopg2.Error:
        return jsonify({"Message":"Error de conexion"}),500

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5011, debug=True)