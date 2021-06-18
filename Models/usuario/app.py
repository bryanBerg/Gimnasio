from flask import Flask, jsonify, request
import psycopg2

app=Flask(__name__)

PSQL_HOST = "gym-db"
#PSQL_HOST ="localhost"
PSQL_USER = "admin"
PSQL_PASS = "esime2021"
PSQL_DB   = "gym_database"
#PSQL_DB   = "gym"

@app.route('/usuario/modification', methods=['PUT'])
def RequestModification():
    try:
        conection=psycopg2.connect(host=PSQL_HOST, database=PSQL_DB, user=PSQL_USER, password=PSQL_PASS)
        cur=conection.cursor()
        data=request.get_json()
        print(data)
        query=f"""select * from usuario where correousuario='{data['correousuario']}' or nombre='{data['nombre']}' and apellidop='{data['apellidop']}'
            or apellidop='{data['apellidop']}' and apellidom='{data['apellidom']}';"""
        cur.execute(query)
        answer=cur.fetchone()
        if answer:
            query=f"""update usuario set correousuario='{data['correousuario']}', telefono='{data['telefono']}',
            nombre='{data['nombre']}', apellidop='{data['apellidop']}', apellidom='{data['apellidom']}'
            where correousuario='{data['correousuario']}' or nombre='{data['nombre']}' and apellidop='{data['apellidop']}'
            or apellidop='{data['apellidop']}' and apellidom='{data['apellidom']}';"""
            cur.execute(query)
            conection.commit()
            cur.close()
            conection.close()
            return jsonify({"Message":"Modificado con exito"}),200
        else:
            return jsonify({"Message":"No existe el usuario"}),404
    except psycopg2.Error:
        return jsonify({"Message":"Fallo la conexion"}),500

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5012, debug=True)