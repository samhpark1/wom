from flask import Flask, jsonify
from dotenv import load_dotenv
from sqlalchemy import text
import os

from db.db_connection import DBConnection

app = Flask(__name__)

load_dotenv()
supa_conn = DBConnection("postgresql", os.getenv("SUPABASE_URL")).sql_conn

try:
    result = supa_conn.execute('SELECT * FROM "Users"').fetchall()
    print(result)
except Exception as e:
    print(f"Error: {e}")

@app.route("/")
def test():
    return jsonify({"message": "lgtm"})

if __name__ == "__main__":
    app.run(debug=True)