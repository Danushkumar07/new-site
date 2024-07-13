from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for products (replace with database integration)
products = [
    {'name': 'Product 1', 'description': 'Description of Product 1', 'image': 'images/product1.jpg'},
    {'name': 'Product 2', 'description': 'Description of Product 2', 'image': 'images/product2.jpg'},
    # Add more products as needed
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/products')
def products():
    return render_template('index.html', products=products)

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
