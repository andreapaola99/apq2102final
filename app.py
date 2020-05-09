# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    #return "<b> Hello World!<b>"
    return render_template("index.html")
@app.route("/Assignment")
def assignment():
    return render_template("Assignment.html")

@app.route("/Class")
def cla():
    return render_template("Class.html")

#start the server
if __name__ == "__main__":
    app.run()