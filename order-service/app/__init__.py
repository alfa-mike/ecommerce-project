from flask import Flask

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return {"message": "Order service"}

if __name__ == '__main__':
    app.run()
