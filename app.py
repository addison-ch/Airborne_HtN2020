# testing
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def landingpage():
    return render_template('landingpage.html')


@app.route('/country/<string:name>')
def country_data(name):
    return render_template('country.html', country=name)


@app.route('/disease')
def disease():
    return render_template('disease.html')


if __name__ == '__main__':
    app.run(debug=True)
