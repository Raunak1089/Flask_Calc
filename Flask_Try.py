from flask import Flask, render_template, request, flash
import math

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

def fac(x):
        num = 1
        i=1
        while i <= int(x):
             num *= i
             i += 1
        return num

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/result", methods=['POST', 'GET'])
def greeter():
	flash(eval(request.form['name_input']))
	return render_template("index.html");

app.run()