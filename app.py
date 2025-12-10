import os
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration variables, pulled from the environment
# DB_HOST will be 'db' in Docker Compose and different in Cloud Run
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

@app.route('/')
def hello_world():
    db_info = f"Attempting connection to DB at: {DB_HOST}:{DB_PORT}"
    return f"<h1>Python API is Live!</h1><p>{db_info}</p>"

@app.route('/health')
def health_check():
    # Health endpoint used by CI/CD & Cloud Run
    return jsonify(status="ok", service="api"), 200

if __name__ == '__main__':
    # Cloud Run injects PORT (usually 8080)
    # Fallback to 5000 for local / Docker Compose
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
