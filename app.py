from flask import Flask  ,request ,render_template
from utils import pred
import mysql.connector
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/prediction" , methods = ['POST'])
def prediction():
    data = request.form
    obj = pred(data)
    result = obj.output()

    return render_template('index.html' , pred = result)

if __name__ == '__main__':
    app.run(debug = True)