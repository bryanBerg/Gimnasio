from flask import Flask, jsonify, request
import psycopg2

app=Flask(__name__)

PSQL_HOST = "gym-db" #"localhost"
PSQL_USER = "admin"
PSQL_PASS = "esime2021"
PSQL_DB   = "gym_database"

@app.route('/membresia/data', methods=['GET'])
def ObtenerMembresias():
    try:
        conection=psycopg2.connect(host=PSQL_HOST, database=PSQL_DB, user=PSQL_USER, password=PSQL_PASS)
        cur=conection.cursor()
        query="select * from membresia;"
        cur.execute(query)
        answer=cur.fetchall()
        print(answer)
        if answer:
            response={"idMembresia":answer}
            return jsonify({"response":response}),200
        else:
            return jsonify({"Message":"No hay Membresias"}),404
    except psycopg2.Error as e:
        answer=-1
    if answer==-1:
        return jsonify({"Error":500, "Message":"Fallo la conexion"})

@app.route('/membresia/modification', methods=['PUT'])
def ActualizarMembresia():
    try:
        conection=psycopg2.connect(host=PSQL_HOST, database=PSQL_DB, user=PSQL_USER, password=PSQL_PASS)
        cur=conection.cursor()
        data=request.get_json()
        query="select * from membresia where idmembresia=%s;"
        cur.execute(query,(data["idmembresia"],))
        answer=cur.fetchall()
        print(answer)
        if answer:
            query=f"update membresia set nombre='{data['nombre']}', costo={data['costo']}, areas='{data['areas']}' where idmembresia={data['idmembresia']}"
            cur.execute(query)
            conection.commit()
            cur.close()
            conection.close()
            return jsonify({"Message":"Modificado con exito"}),200
        else:
            return jsonify({"Message":"No existe esa membresia"}),404
    except psycopg2.Error:
        return jsonify({"Message":"Fallo la conexion"}),500

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5010, debug=True)