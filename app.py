from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Línea modificada para forzar un nuevo build:
    return 'Hello, World! - Versión GitOps Final 🚀' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)