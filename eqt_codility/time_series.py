"""
you are given a dataset temperatures.csv which contain historical monthly data about average land temperatures (in celsius) for some country. your task is to prepare the dataset for modeling, fit three different times series models and calculate forecasts and forecast errors for each of them. you can access dataset using the path "/data/temperature/". the dataset consists of two variables: ds-a data in the format yyyy-mm-01. y average land temperature. please note that the data are not complete. for some datates(e.g 1981-04-01) there is no number in the ds column, and some dates are also missing (e.g. 1980-12-01). Before modelling you are asked to prepare the dataset. In order to complete the task you must write a function named time_series_models_comparison(), which takes no arguments. the function should perform the following steps: prepare the dataset for further analysis with two-step approach. first complete any missing dates, so that time series contains all monthly dates from 1980-01-01 to 2012-12-01, and then fill the missing values in the ds column with the last observed non-null value forward. split the dataset into the training and test set, so that the test set contains the last 24 observations. for the training set fit three models: the ARIMA model, the prophet model and the exponetial smoothing model
"""
import random

import pandas as pd
import pmdarima
import prophet
import sklearn
import statsmodels


def time_series_models_comparison():
    random.seed(123)
    data_set = pd.read_csv("/data/temperature/temperatures.csv")
    data_set["ds"] = pd.to_datetime(data_set["ds"])
    data_set = data_set.set_index("ds")
    data_set = data_set.asfreq("MS")
    data_set = data_set.fillna(method="ffill")
    train_set = data_set[:-24]
    test_set = data_set[-24:]
    arima_model = pmdarima.auto_arima(train_set, seasonal=True, m=12)
    prophet_model = prophet.Prophet()
    prophet_model.fit(
        train_set.reset_index().rename(columns={"ds": "ds", "y": "y"})
    )
    exp_smoothing_model = statsmodels.tsa.holtwinters.ExponentialSmoothing(
        train_set, seasonal_periods=12, trend="add", seasonal="add"
    ).fit()
    arima_forecast = arima_model.predict(n_periods=24)
    prophet_forecast = prophet_model.predict(
        test_set.reset_index().rename(columns={"ds": "ds"})
    )
    exp_smoothing_forecast = exp_smoothing_model.predict(
        start=test_set.index[0], end=test_set.index[-1]
    )
    arima_forecast_error = sklearn.metrics.mean_squared_error(
        test_set, arima_forecast, squared=False
    )
    prophet_forecast_error = sklearn.metrics.mean_squared_error(
        test_set, prophet_forecast["yhat"], squared=False
    )
    exp_smoothing_forecast_error = sklearn.metrics.mean_squared_error(
        test_set, exp_smoothing_forecast, squared=False
    )
    return (
        arima_forecast_error,
        prophet_forecast_error,
        exp_smoothing_forecast_error,
    )
