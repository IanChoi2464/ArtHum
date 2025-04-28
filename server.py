from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/original')
def original():
   return render_template('original.html')

@app.route('/a')
def a():
   return render_template('a.html')

@app.route('/b')
def b():
   return render_template('b.html')

@app.route('/c')
def c():
   return render_template('c.html')

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')

if __name__ == '__main__':
   app.run(debug = True, port=5001)
