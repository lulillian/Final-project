from flask import Flask, render_template, request
from polygon_api import get_daily_open_close, get_company_info, ticker_news, balance_sheet


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
    values=get_daily_open_close(stock_ticker)
    info=get_company_info(stock_ticker)
    news = ticker_news(stock_ticker)
    balance = balance_sheet(stock_ticker)
    return render_template('results.html',values=values,info=info,news=news,balance=balance)

# @app.get()


if __name__ == '__main__':
    app.run(debug=True)
