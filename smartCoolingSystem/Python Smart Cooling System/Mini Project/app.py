#Lutfi Lais 1946853
#Idris 1948363
#Webserver
from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


app.run(debug=True,host='0.0.0.0') #0.0.0.0 => accessible to any device on the network

