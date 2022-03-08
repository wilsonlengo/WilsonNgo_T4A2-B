from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'description': 'It is a phone', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'description': 'It is a laptop', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'description': 'It is a keyboard', 'price': 150}
    ]
    return render_template("market.html", items=items)


