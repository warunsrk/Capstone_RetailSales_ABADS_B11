# Capstone_RetailSales_ABADS_B11
Capstone Project on Retail Sales where the retailer wants to understand what kind of customers respond to different campaigns.
# Retail Customer Analysis

This repository contains the analysis of customer data from a leading retail giant. The dataset includes information on customer demographics, purchase behaviour, and responses to various marketing campaigns. The study aims to understand customer behaviour and their reactions to marketing efforts.

## Table of Contents

- [Data Description](#data-description)
- [Data Preparation](#data-preparation)
- [Data Quality and Check](#data-quality-and-check)
- [Business Analysis and Hypothesis](#business-analysis-and-hypothesis)
- [Requirements](#requirements)
- [Usage](#usage)

## Data Description

The dataset consists of three main files:

1. **Demographics Data (`demographics.txt`)**: Contains customer demographics information.
2. **Purchase Behavior Data (`behaviour.json`)**: Contains information on customer purchase behaviour over the last 2 years.
3. **Campaign Response Data (`campaign.json`)**: Contains customer responses to various marketing campaigns.

### Demographics Data

- `ID`: Customer's unique identifier
- `Year_Birth`: Customer's birth year
- `Education`: Customer's education level
- `Marital_Status`: Customer's marital status
- `Income`: Customer's yearly household income
- `Kidhome`: Number of children in customer's household
- `Teenhome`: Number of teenagers in customer's household
- `Dt_Customer`: Date of customer's enrollment with the company
- `Country`: Customer's location

### Purchase Behavior Data

- `Recency`: Number of days since customer's last purchase
- `MntWines`: Amount spent on wine in the last 2 years
- `MntFruits`: Amount spent on fruits in the last 2 years
- `MntMeatProducts`: Amount spent on meat in the last 2 years
- `MntFishProducts`: Amount spent on fish in the last 2 years
- `MntSweetProducts`: Amount spent on sweets in the last 2 years
- `MntGoldProds`: Amount spent on gold in the last 2 years
- `NumDealsPurchases`: Number of purchases made with a discount
- `NumWebPurchases`: Number of purchases made through the company's website
- `NumCatalogPurchases`: Number of purchases made using a catalog
- `NumStorePurchases`: Number of purchases made directly in stores
- `NumWebVisitsMonth`: Number of visits to the company's website in the last month

### Campaign Response Data

- `AcceptedCmp1`: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
- `AcceptedCmp2`: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
- `AcceptedCmp3`: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
- `AcceptedCmp4`: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
- `AcceptedCmp5`: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
- `Response`: 1 if customer accepted the offer in the last campaign, 0 otherwise
- `Complain`: 1 if customer complained in the last 2 years, 0 otherwise

## Data Preparation

1. **Data Loading**: Loaded the demographic, behaviour, and campaign data from respective files.
2. **Data Cleaning**: 
   - Removed extra spaces in column names.
   - Converted the `Income` column to a numeric type.
   - Merged the datasets on the `ID` column.
3. **Data Consolidation**: Created a consolidated DataFrame containing all relevant information from the three datasets.

## Data Quality and Check

### 1. Create a Consolidated View of Data

- **Loaded and merged** the datasets from the three files: demographics, behaviour, and campaign response.
- Ensured consistent data types and removed any extra spaces in column names.

### 2. Data Cleaning

Identified variables needing cleaning:
- `Income`: Converted to a numeric type.
- `Dt_Customer`: Converted to a datetime type.
- Checked for missing values and handled them appropriately.

### 3. Data Quality Report

Performed univariate analysis for continuous and categorical variables:

#### Continuous Variables

- Calculated the percentage of missing values, percentage of zero values, mean, percentiles (25th, 50th, 75th, 90th, 95th), minimum, and maximum.
- Generated a report showing these statistics.

#### Categorical Variables

- Calculated the percentage of missing values and the number of unique values.
- Generated a report showing these statistics.

### 4. Extreme Values

- Identified extreme values in variables representing income, amount spent on various categories, and recency of purchase.
- Used box plots and calculated the upper fence to determine potential outliers.

## Business Analysis and Hypothesis

### 1. Hypotheses Testing

- **Hypothesis 1**: Customers who spend more on certain product categories are more likely to respond to marketing campaigns.
  - Performed t-tests to compare the means of spending between responders and non-responders for each campaign.

- **Hypothesis 2**: Recent customers complain less compared to older customers.
  - Classified customers as recent or older based on their enrollment date.
  - Performed a t-test to compare the mean complaint rates between recent and older customers.

### 2. Funnel Analysis

- Created a funnel analysis showing the percentage of unique customers who accepted each campaign.
- Plotted the results to visualize the acceptance rates across different campaigns.

### 3. Income Impact Analysis

- Analyzed how income impacts the amount spent on wine, meat products, gold products, and fish products.
- Used scatter plots and calculated correlation coefficients to understand the relationships between income and spending on these categories.


### Task 4: Complaint Analysis

1. **Tested Hypothesis on Complaints**:
   - Tested the hypothesis that recent customers complain less compared to older customers.
   - Classified customers as recent or older based on their enrollment date.
   - Performed a t-test to compare the mean complaint rates between recent and older customers.

### Task 5: Campaign Acceptance Analysis

1. **Analyzed Campaign Acceptance**:
   - Investigated if customers who accept the offer in the first campaign also accept offers in other campaigns.

### Task 6: Customer Profile Analysis

1. **Profile of Responders vs. Non-Responders**:
   - Analyzed and compared the profiles of customers who responded to campaigns versus those who did not.



# Customer Response Prediction

This project involves building and deploying a machine-learning model to predict customer responses to marketing campaigns. The model is deployed using Flask to provide a web interface for users to input customer data and receive predictions.

**Data Preparation**

**Steps Followed**
- Load the Data: The demographic, behaviour, and campaign data were loaded from respective files.
- Data Cleaning and Preprocessing: The data were cleaned by removing extra spaces in column names and converting income values to a numeric format.
- Merge Data: The datasets were merged on the ID column to create a consolidated data frame.
- Handle Missing Values: Missing values were handled using the SimpleImputer with the strategy set to 'mean'.

  ### Model Training

**Steps Followed**

- Feature and Target Selection: Selected relevant features and target variable (Response).
- Convert Categorical Variables: Convert categorical variables to dummy variables.
- Split Data: Split the data into training and testing sets.
- Train Models: Trained both Logistic Regression and Random Forest models.
- Evaluate Models: Evaluated the models using classification metrics.
- Save the Best Model: Saved the Random Forest model as it performed better along with the imputer.

### Model Evaluation

**Logistic Regression Model**
- The Logistic Regression model performance:
  Logistic Regression Model
              precision    recall  f1-score   support

           0       0.84      0.89      0.86       668
           1       0.65      0.54      0.59       232

    accuracy                           0.79       900
   macro avg       0.74      0.71      0.72       900
weighted avg       0.78      0.79      0.78       900

Confusion Matrix:
[[595  73]
 [106 126]]


**Random Forest Model**
- The Random Forest model performance:
  Random Forest Model
              precision    recall  f1-score   support

           0       0.87      0.91      0.89       668
           1       0.72      0.62      0.67       232

    accuracy                           0.83       900
   macro avg       0.79      0.76      0.78       900
weighted avg       0.83      0.83      0.83       900

Confusion Matrix:
[[609  59]
 [ 89 143]]


**Model Preference**

We chose the Random Forest model because it outperformed the Logistic Regression model across all key metrics:

- Higher accuracy: 0.83 compared to 0.79
- Better precision and recall for both classes
- Higher F1-score

### Model Deployment

**Steps Followed**

- Create Flask Application: Set up a Flask application to serve the model.
- Load Model and Imputer: Loaded the trained Random Forest model and the imputer.
- Create HTML Form: Created an HTML form to collect user input.
- Handle Form Submissions: Processed form submissions to collect input data, preprocess it, and use the model to make predictions.

**Flask Application Code**
The Flask application (app.py) was created to handle user input and provide predictions based on the trained model.

**HTML Form**
An index.html file was created to provide a user-friendly interface for inputting customer data.

### Outcomes and Inferences

**Model Performance**: The Random Forest model performed better than the Logistic Regression model, with an accuracy of 83% and better precision, recall, and F1-scores.
**Feature Importance**: Features like Income, MntMeatProducts, MntWines, and Recency were found to be significant in predicting customer response.
**Model Deployment**: The model was successfully deployed using Flask, providing a user-friendly prediction interface.




## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
