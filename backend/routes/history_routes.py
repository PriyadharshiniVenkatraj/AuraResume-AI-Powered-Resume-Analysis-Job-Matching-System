from flask import Blueprint, jsonify
import sqlite3

history_bp = Blueprint("history", __name__)

@history_bp.route("/history/<email>", methods=["GET"])
def get_history(email):

    conn = sqlite3.connect("history.db")
    c = conn.cursor()

    c.execute("SELECT * FROM history WHERE email=?", (email,))
    rows = c.fetchall()

    conn.close()

    return jsonify(rows)