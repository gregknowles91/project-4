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

Built an interactive Flask web app to predict the power-to-price ratio.
The user enters inputs like price, horsepower, mileage, vehicle age, and brand using a simple HTML form.
The model then returns a predicted value, making it easy to assess a car’s performance value.
 
 Questions 

Q1: What factors impact the power-to-price ratio the most?
A: Vehicle age, horsepower, and brand are major drivers. Mid-aged cars (6–12 yrs) and diesel engines often offer better value.

Q2: Can power-to-price ratio be predicted accurately?
A: Yes. The Random Forest model achieved good accuracy, capturing non-linear patterns in the data.


Q3: What does the power-to-price ratio reveal about luxury brands compared to others?
A: From the bar chart showing the top and bottom 15 brands, we observed that luxury brands tend to offer a lower power-to-price ratio. This means that for every $1,000 spent, these brands generally deliver less horsepower, reflecting a premium cost for branding, design, and features rather than raw performance. In contrast, non-luxury and performance-focused brands often provide higher horsepower per dollar, offering better value in terms of engine power.

  Requirements python >= 3.10 tensorflow >= 2.15 pandas >= 2.2 scikitlearn >= 1.4 matplotlib >= 3.8 jupyterlab Install via pip install -r requirements.txt (file included) or the conda snippet in Quick Start.

  Author & Licence Delaram Dadfarnia– Data Science Bootcamp Student ✉️ delaramrealtyca@gmail.com 🔗  • 
