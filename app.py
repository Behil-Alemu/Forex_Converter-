from crypt import methods
from decimal import Decimal
from unittest import result
from flask import Flask, redirect,render_template,flash, request,session
from forex_python.converter import CurrencyRates
from flask_debugtoolbar import DebugToolbarExtension
import requests


app=Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# c = CurrencyRates()
# c.get_rate('USD', 'ISK')
# c.convert('USD','ISK', 10)
# c.get_rates('USD')

@app.route("/")
def start_converter():
    """show the converter page"""
    session["Responses"] = []

    return render_template("start_converter.html")




@app.route("/result", methods=["POST"])
def convert():
    """show the converted currency"""
    # input = session['input']

    c = CurrencyRates()
    amount = float(request.form['amount'])
    from_cur = (request.form.get('from')).upper()
    to_cur = (request.form.get('to')).upper()

    result = c.convert(from_cur,to_cur, amount)
    # try:
    #     int_amount = isinstance(amount, int)
    #     float_amount = isinstance(amount, float)
    #     if int_amount or float_amount:
    #         return amount
    # except ValueError:
    #     flash('Not a valid code')
    #     return redirect('/')
    # except TypeError:
    #     flash('Not a valid code')
    #     return redirect('/')
    
    # if isinstance(from_cur, str) and len(from_cur)== 3:
    #     redirect('/')
    #     flash('hi')


            
        
        
    return render_template("converted.html",from_cur=from_cur, to_cur=to_cur, result=result)


@app.route('/return-home')
def return_home():
    """Return back home from result page"""

    return redirect('/')
