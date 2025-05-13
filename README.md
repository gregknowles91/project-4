# 📊 Project 4: Predicting Used Car Resale Value with Machine Learning

This project explores how machine learning can be used to predict the resale price of used vehicles and analyze depreciation trends based on car age and kilometers driven.

## Machine Learning Models Used

### 1. Linear Regression
- Simple baseline model
- Captures linear trends but performs poorly with non-linear relationships

### 2. Random Forest Regressor (Best Performing)
- Ensemble of decision trees
- Handles non-linearities, interactions, and outliers well
- Tuned using GridSearchCV for best accuracy (highest R², lowest RMSE)

### 3. Gradient Boosting Regressor
- Boosting model that improves sequentially
- Strong performance, but slightly behind tuned Random Forest in accuracy

##Feature Engineering

- **car_age**: Derived from model_year (2025 - model_year)
- **engine_hp**: Horsepower extracted from engine text (e.g., "150HP 2.0L")
- **milage**: Distance driven in km
- **fuel_type**: Encoded and mapped for visual clarity
- Additional encoded features: brand, accident history, model

## Depreciation Analysis

### Question: How does depreciation affect resale value based on age and kilometers driven?

**Approach:**
- Regression and comparative analysis using car_age and milage
- Segmented by fuel_type for group-level insights

**Visualizations:**
- **Line chart** of average price by car age
- **Line chart** of average price by age grouped by fuel_type
- **Scatter plot** of price vs. age with mileage bins

**Outcome:**
- Clear negative correlation between car_age and price (price drops with age)
- Higher milage accelerates value loss
- Fuel types depreciate at different rates (e.g., Hybrid vs. Gasoline vs. Diesel)

##Questions Answered

- **How does depreciation affect resale value based on age and kilometers driven?**
  ✔️ Modeled using car_age and milage  
  ✔️ Visualized with grouped charts

- **Can price be predicted using available features?**
  ✔️ Yes — with high accuracy using Random Forest

- **Do fuel types impact depreciation trends?**
  ✔️ Yes — shown via grouped line charts

- **Is the problem linear or nonlinear?**
  ✔️ Nonlinear — Random Forest and Gradient Boosting outperform Linear Regression

##How to Use

1. Open in VS Code or Jupyter Lab
2. Run `full_car_price_ml_notebook_optimized.ipynb`
3. Ensure packages: pandas, numpy, sklearn, plotly
4. Inspect visuals and model evaluation metrics
