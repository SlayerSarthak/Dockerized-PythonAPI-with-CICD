import os
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration variables, pulled from the Docker environment
# DB_HOST will be 'db' when running inside Docker Compose
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

@app.route('/')
def hello_world():
    # Shows the connection info loaded from the environment
    db_info = f"Attempting connection to DB at: {DB_HOST}:{DB_PORT}"
    return f"<h1>Python API is Live!</h1><p>{db_info}</p>"

@app.route('/health')
def health_check():
    # Essential for CI/CD checks (Liveness/Readiness in Kubernetes)
    # In a real app, this would verify the database connection.
    return jsonify(status="ok", service="api"), 200

if __name__ == '__main__':
    # Flask runs on port 5000 by default, exposed via Docker
    app.run(host='0.0.0.0', port=5000)
