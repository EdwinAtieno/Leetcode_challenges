import pandas as pd
from fbprophet import Prophet
from pmdarima import auto_arima
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def prepare_and_forecast(dataset_path):
    # Step 1: Prepare the dataset
    data = pd.read_csv(dataset_path)
    data["ds"] = pd.to_datetime(data["ds"])
    complete_dates = pd.date_range(
        start="1980-01-01", end="2012-12-01", freq="MS"
    )
    data = data.set_index("ds").reindex(complete_dates).reset_index()
    data["y"] = data["y"].fillna(method="ffill")

    # Step 2: Split the dataset into training and test sets
    train = data[:-24]
    test = data[-24:]

    # Step 3: Fit the ARIMA model
    arima_model = auto_arima(
        train["y"], seasonal=True, suppress_warnings=True
    )
    arima_forecast = arima_model.predict(n_periods=24)

    # Step 3: Fit the Prophet model
    prophet_model = Prophet(
        yearly_seasonality=True,
        daily_seasonality=False,
        seasonality_mode="additive",
        growth="linear",
        interval_width=0.95,
    )
    prophet_model.fit(train.rename(columns={"ds": "ds", "y": "y"}))
    prophet_forecast = prophet_model.make_future_dataframe(
        periods=24, freq="MS"
    )
    prophet_forecast = prophet_model.predict(prophet_forecast)[-24:]

    # Step 3: Fit the Exponential Smoothing model
    ets_model = ExponentialSmoothing(
        train["y"], seasonal="add", seasonal_periods=12
    )
    ets_results = ets_model.fit()
    ets_forecast = ets_results.forecast(steps=24)

    # Step 4: Calculate mean squared errors
    mse_arima = mean_squared_error(test["y"], arima_forecast)
    mse_prophet = mean_squared_error(test["y"], prophet_forecast["yhat"])
    mse_ets = mean_squared_error(test["y"], ets_forecast)

    return {
        "ARIMA": {"Forecast": arima_forecast, "MSE": mse_arima},
        "Prophet": {
            "Forecast": prophet_forecast["yhat"].values,
            "MSE": mse_prophet,
        },
        "Exponential_Smoothing": {"Forecast": ets_forecast, "MSE": mse_ets},
    }


# Usage example
dataset_url = (
    "https://drive.google.com/uc?id=1Y1GmY8RnVQ0D3e3ZpY2y6t5V9y7t9Z8j"
)
result = prepare_and_forecast(dataset_url)
print(result)
