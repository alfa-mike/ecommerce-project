from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api_gateway():
    return {"message": "API Gateway"}

if __name__ == '__main__':
    app.run()
    