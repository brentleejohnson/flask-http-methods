from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def log():
    return render_template('shoppinglist.html')


@app.route('/table', methods=['POST'])
def table():
    item_name = request.form['item']
    item_id = request.form['itemid']
    item_qty = request.form['quantity']
    item_price = request.form['price']
    return render_template('showitems.html', item_price=item_price, item_name=item_name, item_id=item_id, item_qty=item_qty)


if __name__ == '__main__':
    app.run(debug=True)
