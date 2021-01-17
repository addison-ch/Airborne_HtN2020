from flask import Flask, render_template, request, redirect
from disease import get_worse_disease

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
    name = name.title()
    disease = get_worse_disease(name)
    disease = disease.split()[0]
    if disease == 'Influenza':
        return render_template('influenza.html', country=name, d=disease)
    elif disease == 'HIV':
        return render_template('hiv.html', country=name, d=disease)
    elif disease == 'Malaria':
        return render_template('malaria.html', country=name, d=disease)
    elif disease == 'Cholera':
        return render_template('cholera.html', country=name, d=disease)
    elif disease == 'Tuberculosis':
        return render_template('tuberculosis.html', country=name, d=disease)


if __name__ == '__main__':
    app.run(debug=True)
