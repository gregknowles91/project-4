---Car Price Prediction
A data-driven machine learning project designed to predict used car prices based on key features such as brand, mileage, transmission type, fuel type, engine horsepower, and more. This project involves data cleaning, exploratory data analysis, model training, and deployment-ready prediction functionality using models like Random Forest Regressor and XGBoost.

📊 Features
Data preprocessing & feature engineering

Outlier detection & removal using IQR

Exploratory Data Analysis (EDA) with visualizations

OneHotEncoding of categorical features

Model training using:

Random Forest Regressor

XGBoost Regressor

Model evaluation using R², MAE, and RMSE

Gradio interface for real-time predictions

🧰 Tech Stack
Languages: Python

Libraries:
pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, gradio

📂 Dataset
car_data.csv: Raw dataset of used cars.

old_car_data.csv: Cleaned version after preprocessing and outlier removal.

🛠️ Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the notebook or script to train the model.
Ensure you have the dataset in the root directory.

(Optional) Run Gradio app:

bash
Copy
Edit
python app.py
🔍 Exploratory Data Analysis
Distribution plots for price and miles

Scatter plot for price vs. miles

Boxplot of price by fuel type

Average price by top 15 brands

Heatmap for correlation between price, year, miles, engine(hp)

🧪 Model Evaluation
Random Forest Regressor
R² Score: 0.89+

MAE: ~1500

RMSE: ~2300

XGBoost Regressor
R² Score: 0.90+

MAE: ~1400

RMSE: ~2200

📌 Top 5 Features (Random Forest):

Mileage

Year

Brand

Engine (HP)

Fuel type

🔮 Prediction Function
Example prediction input:

python
Copy
Edit
predict_price('FIAT', 2013, 'Manual', 'Gasoline', 2, 30068, 135)
Returns:

nginx
Copy
Edit
Predicted Price: $5,800.00