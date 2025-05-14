# project-4
# Used Car Power-to-Price Analysis and Prediction

This project analyzes and predicts the power-to-price ratio of used cars to identify which brands and models provide the best value in terms of horsepower per dollar.

1. Data Preprocessing
    •    Cleaned raw CSV file with car listings
    •    Extracted numeric features from text fields (e.g., price, engine size)
    •    Created new variables like power_to_price, vehicle_age, and age_group
    •    Dropped irrelevant columns and handled missing values

2. Exploratory Data Analysis

We used various graphs to analyze how the power-to-price ratio varies by:
    •    Brand – Ranked all brands, then highlighted top and bottom 15 brands
    •    Model – Identified top 20 models offering the best value
    •    Vehicle Age – Found that mid-aged vehicles (6–20 years) give the highest value
    •    Fuel Type – Diesel and flex fuel showed higher power-to-price ratios
    •    Scatter Plot – Visualized the relationship between engine horsepower and price across brands and age groups

3. Machine Learning Model

To predict the power-to-price ratio, we built a pipeline using:
    •    Preprocessing: StandardScaler, OneHotEncoder for numeric and categorical data
    •    Model: RandomForestRegressor
    •    Optimization: Used RandomizedSearchCV to tune hyperparameters (n_estimators, max_depth)

Model Evaluation
    •    RMSE and MAE were calculated on the test set
    •    Predicted vs. Actual scatter plot showed a strong linear trend, indicating the model performed well in estimating power-to-price values

4. Key Visualizations
    •    Bar charts of top/bottom brands and models by power-to-price
    •    Average value comparisons by age and fuel type
    •    Scatter plot showing price vs. horsepower
    •    Predicted vs. Actual power-to-price chart

5. Usage

Run the notebook end-to-end to reproduce:
    •    The data wrangling and feature engineering steps
    •    Insightful visual analyses
    •    A trained prediction model with evaluation metrics
    •    Saved model using joblib for reuse
    
 6. Power-to-Price Prediction Web App

         I developed an interactive web application using Flask and HTML that predicts the power-to-price ratio of used cars. The user inputs key car attributes such as price, vehicle age, mileage, horsepower, and selects the brand from a dropdown menu. Once submitted, the trained machine learning model returns the predicted power-to-price ratio. This tool provides a quick and intuitive way to evaluate the performance value of a car based on its specifications.
