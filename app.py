from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello ArgoCD is Cool  mi papá'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
