from flask import Flask, render_template, request, redirect, url_for, session
from polygon_api import get_daily_open_close, get_company_info, ticker_news, balance_sheet
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


portfolio = []

@app.get('/')
def hello():
    return render_template('stock_search.html')

@app.post('/')
def results():
    stock_ticker=request.form['stock_ticker']
    values=get_daily_open_close(stock_ticker)
    info=get_company_info(stock_ticker)
    news = ticker_news(stock_ticker)
    balance = balance_sheet(stock_ticker)

    session['values'] = values
    session['info'] = info
    session['news'] = news
    session['balance'] = balance
    return redirect(url_for('route_results'))

@app.route('/results')
def route_results():
    values = session.get('values')
    info = session.get('info')
    news = session.get('news')
    balance = session.get('balance')
    return render_template('results.html',values=values,info=info,news=news,balance=balance)

@app.post('/results')
def port():
    return render_template('portfolio.html')
# @app.get()

@app.route('/portfolio')
def viewportfolio():
    info = session.get('info')
    if(info[3] not in portfolio):
        portfolio.append(info[3])
    return render_template('portfolio.html',portfolio=portfolio)

if __name__ == '__main__':
    app.run(debug=True)
