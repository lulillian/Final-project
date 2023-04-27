from flask import Flask, render_template, request
from polygon_api import get_daily_open_close, get_open


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'

@app.get('/form')
def origin():
    return render_template('stock_search.html')

@app.post('/form')
def results():
    stock_ticker=request.form['stock_ticker']
    openning_price=get_open(stock_ticker)
    return render_template('results.html',openning_price_html=openning_price)





if __name__ == '__main__':
    app.run(debug=True)
