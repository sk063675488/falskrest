from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/abouts')
def abouts():
    return render_template('abouts.html')



if __name__ == '__main__':
    app.run(debug=True)