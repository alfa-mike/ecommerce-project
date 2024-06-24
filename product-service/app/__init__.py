from flask import Flask

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return {"message": "Product service"}

if __name__ == '__main__':
    app.run()
