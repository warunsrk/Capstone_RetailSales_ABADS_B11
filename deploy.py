from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('retail_sale_model.sav', 'rb'))
@app.route('/')
def home():
    result= ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    age = float(request.form['Age'])
    education = float(request.form['Education'])
    marital_status = float(request.form['Marital_Status'])
    income = float(request.form['Income'])
    kid = float(request.form['Kidhome'])
    teen = float(request.form['Teenhome'])
    country = float(request.form['Country'])
    recency = float(request.form['Recency'])
    wine = float(request.form['MntWines'])
    fruit = float(request.form['MntFruits'])
    meat = float(request.form['MntMeatProducts'])
    fish = float(request.form['MntFishProducts'])
    sweet = float(request.form['MntSweetProducts'])
    gold = float(request.form['MntGoldProds'])
    result = model.predict([[age, education, marital_status, income, kid, teen, country, recency, 
                             wine, fruit, meat, fish, sweet, gold]])[0]
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)

