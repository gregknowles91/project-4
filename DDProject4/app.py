from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("power_to_price_model.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        input_data = {
            'price_numeric $': float(request.form['price']),
            'vehicle_age': int(request.form['age']),
            'milage_numeric': float(request.form['mileage']),
            'engine_hp HP': float(request.form['horsepower']),
            'brand': request.form['brand']
        }
        df = pd.DataFrame([input_data])
        prediction = round(model.predict(df)[0], 2)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

