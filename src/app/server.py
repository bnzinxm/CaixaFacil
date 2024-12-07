from flask import (
    Flask, 
    jsonify
)

import yaml
import mysql.connector
from mysql.connector import Error
from src.db.database import Database


app = Flask(__name__)
conf = data = yaml.safe_load(open("../config/.yaml"))

# Configurar o banco de dados

file = "../config/.yaml"

Database.load_config(file)

HOST = Database.get_host(file)
PORT = Database.get_port(file)
USER = Database.get_user(file)
PASSWORD = Database.get_password(file)
NAME = Database.get_name(file)
DATABASE = "mysql"

# Essa aqui vai ser a rota de teste
@app.route("/api", methods=["GET"])
def home():
    print("API Rodando na porta: 5000") # Debug
    
    return "Api funcionando aqui!"

@app.route("/api/db", methods=["GET"])

def check_db():
    try:
        # Aqui iremos tentar se conectar com o banco de dados para testar se está funcionando
        connection = mysql.connector.connect(
            HOST,
            PORT,
            USER,
            PASSWORD,
            NAME
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            return jsonify({
                "status": "success",
                "message": "Conexão com o banco de dados bem sucedida",
                "server_version": db_info
            }), 200
    except Error as e:
        return jsonify({
            "status": "error",
            "message": f"Erro ao conectar com o banco de dados: {e}"
        }), 500
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexão com o banco de dados bem sucedida!")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
    