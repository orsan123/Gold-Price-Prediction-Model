from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
import joblib

app = Flask(
    __name__,
    template_folder=r'C:\Users\pc\OneDrive\Documents\Career Based Projects\Gold_Price_Prediction\templates'
)
app.secret_key = 'your_secret_key'

model = joblib.load(
    r"C:\Users\pc\OneDrive\Documents\Career Based Projects\Gold_Price_Prediction\model\prophet_model.pkl"
)  # Loading the model and forecast data
preds = pd.read_csv(
    r"C:\Users\pc\OneDrive\Documents\Career Based Projects\Gold_Price_Prediction\data\processed\forecast.csv"
)
preds['ds'] = pd.to_datetime(preds['ds'])


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            return redirect(url_for("home"))
        else:
            flash("Username or password is wrong. Please try again.")
            return render_template('login.html')

    return render_template('login.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/predict", methods=["GET", "POST"])
def index():
    prediction = None
    selected_date = None
    min_date = preds['ds'].min().date()
    max_date = preds['ds'].max().date()

    if request.method == "POST":
        selected_date = request.form.get("date")
        selected_date = pd.to_datetime(selected_date)

        result = preds[preds['ds'] == selected_date]
        if not result.empty:
            prediction = round(result.iloc[0]['yhat'], 2)
        else:
            prediction = "No prediction available for this date."

    return render_template(
        'index.html',
        prediction=prediction,
        selected_date=selected_date,
        min_date=min_date,
        max_date=max_date
    )


@app.route("/forecast")
def forecast():
    trained_data = pd.read_csv(
        r"C:\Users\pc\OneDrive\Documents\Career Based Projects\Gold_Price_Prediction\data\raw\gold_and_usdx.csv"
    )

    head_data = trained_data.head(5).to_html(classes='table table-striped', index=False)
    tail_data = trained_data.tail(5).to_html(classes='table table-striped', index=False)

    preds_json = preds.to_json(orient='records')
    trained_json = trained_data.to_json(orient='records')

    return render_template(
        'forecast.html',  # Changed to HTML template
        head_data=head_data,
        tail_data=tail_data,
        preds_json=preds_json,
        trained_json=trained_json
    )


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)