from flask import Flask 
#from flask import request

app = Flask(__name__)

@app.route('/') 
def index():
    #headers = request.headers
    return "hello voting"

if __name__ == "__main__":
    app.run(host='0.0.0.0')