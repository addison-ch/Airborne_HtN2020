# testing
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def landingpage():
    return render_template('landingpage.html')


@app.route('/', methods=['POST'])
def search():
    keyword = request.form['country']
    return redirect("/country/"+keyword)


@app.route('/country')
def wrongpage():
    return redirect('/')


@app.route('/country/<string:name>')
def country_data(name):
    return render_template('country.html', country=name)


if __name__ == '__main__':
    app.run(debug=True)
