from flask import Flask, render_template, request, jsonify
import ssl

app = Flask(__name__)

# Пример данных о товарах
products = [
    {"id": 1, "name": "Товар 1", "price": 10.99, "image": "https://cdn.shopify.com/s/files/1/0606/7250/8087/collections/smash.png?v=1684563892"},
    {"id": 2, "name": "Товар 2", "price": 19.98, "image": "https://cdn.shopify.com/s/files/1/0606/7250/8087/collections/smash.png?v=1684563892"},
    {"id": 3, "name": "Товар 3", "price": 5.99, "image": "https://cdn.shopify.com/s/files/1/0606/7250/8087/collections/smash.png?v=1684563892"},
    {"id": 4, "name": "Товар 4", "price": 14.99, "image": "https://cdn.shopify.com/s/files/1/0606/7250/8087/collections/smash.png?v=1684563892"},
    {"id": 5, "name": "Товар 5", "price": 14.99, "image": "https://cdn.shopify.com/s/files/1/0606/7250/8087/collections/smash.png?v=1684563892"},
]


@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context,  debug=True, threaded=True)