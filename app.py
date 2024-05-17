from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Data storage (replace with database in production)
orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    customer_name = request.form['customer_name']
    address = request.form['address']
    fuel_quantity = request.form['fuel_quantity']
    
    order = {
        'customer_name': customer_name,
        'address': address,
        'fuel_quantity': fuel_quantity
    }
    orders.append(order)
    
    return redirect(url_for('order_confirmation'))

@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
