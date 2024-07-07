from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and the imputer
model = joblib.load('random_forest_model.pkl')
imputer = joblib.load('imputer.pkl')

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    data = {
        "Year_Birth": int(request.form.get('Year_Birth')),
        "Income": float(request.form.get('Income')),
        "Kidhome": int(request.form.get('Kidhome')),
        "Teenhome": int(request.form.get('Teenhome')),
        "Recency": int(request.form.get('Recency')),
        "MntWines": float(request.form.get('MntWines')),
        "MntFruits": float(request.form.get('MntFruits')),
        "MntMeatProducts": float(request.form.get('MntMeatProducts')),
        "MntFishProducts": float(request.form.get('MntFishProducts')),
        "MntSweetProducts": float(request.form.get('MntSweetProducts')),
        "MntGoldProds": float(request.form.get('MntGoldProds')),
        "NumDealsPurchases": int(request.form.get('NumDealsPurchases')),
        "NumWebPurchases": int(request.form.get('NumWebPurchases')),
        "NumCatalogPurchases": int(request.form.get('NumCatalogPurchases')),
        "NumStorePurchases": int(request.form.get('NumStorePurchases')),
        "NumWebVisitsMonth": int(request.form.get('NumWebVisitsMonth')),
        "Education": request.form.get('Education'),
        "Marital_Status": request.form.get('Marital_Status'),
        "Country": request.form.get('Country')
    }
    df = pd.DataFrame([data])
    
    # Define feature columns
    features = ['Year_Birth', 'Income', 'Kidhome', 'Teenhome', 'Recency', 
                'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 
                'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 
                'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 
                'NumWebVisitsMonth']

    # Convert categorical columns to dummy variables
    df = pd.get_dummies(df, columns=['Education', 'Marital_Status', 'Country'], drop_first=True)
    
    # Ensure all necessary columns are present
    for col in features:
        if col not in df.columns:
            df[col] = 0

    # Handle missing values using SimpleImputer
    df[features] = imputer.transform(df[features])

    # Make prediction
    prediction = model.predict(df[features])
    return render_template('index.html', prediction=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
