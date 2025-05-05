print("Flask app is starting..")
print("Running on http://127.0.0.1:5050")

from flask import Flask, render_template, redirect, url_for, session, request
from products import products

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    session.modified = True  # To ensure session changes are saved
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = [p for p in products if p['id'] in session.get('cart', [])]
    return render_template('cart.html', cart=cart_items)

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='127.0.0.1')
