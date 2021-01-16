# testing
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/disease')
def disease():
    return render_template('disease.html')


if __name__ == '__main__':
    app.run(debug=True)