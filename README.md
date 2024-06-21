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
2. **Purchase Behavior Data (`behaviour.json`)**: Contains information on customer purchase behavior over the last 2 years.
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

1. **Data Loading**: Loaded the demographic, behavior, and campaign data from respective files.
2. **Data Cleaning**: 
   - Removed extra spaces in column names.
   - Converted the `Income` column to a numeric type.
   - Merged the datasets on the `ID` column.
3. **Data Consolidation**: Created a consolidated DataFrame containing all relevant information from the three datasets.

## Data Quality and Check

### 1. Create a Consolidated View of Data

- **Loaded and merged** the datasets from the three files: demographics, behavior, and campaign response.
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

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
