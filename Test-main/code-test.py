import sqlite3
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# WEAKNESS 1: Hardcoded Sensitive Credential
# Scanners look for variable names like 'key', 'password', or 'token' followed by a string.
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc" 

@app.route("/user-lookup")
def lookup():
    user_id = request.args.get("id")
    
    # WEAKNESS 2: SQL Injection (SQLi)
    # Using f-strings or concatenation instead of parameterized queries.
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'" 
    cursor.execute(query)
    
    # WEAKNESS 3: Reflected Cross-Site Scripting (XSS)
    # Returning raw user input back to the browser without escaping/sanitizing.
    return render_template_string(f"<h1>Results for {user_id}</h1>")

if __name__ == "__main__":
    app.run(debug=True)
