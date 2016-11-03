from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user="Admin")

@app.route('/reddit')
def reddit():
    # return render_template('reddit.html', title='reddit', user='Admin')
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

