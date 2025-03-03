import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from django.shortcuts import render
import io
import base64

# Create your views here.

def predict_energy_consumption(request):
    df = pd.read_csv('forecast/data/solar_cleaned.csv')

    # print(df.head())

    df['DATE'] = pd.to_datetime(df['DATE'])

    df.set_index('DATE', inplace=True)

    # print(df.head())

    gdf = pd.read_csv('forecast/data/grid_cleaned.csv')
    # print(gdf.head())

    gdf['MONTH'] = pd.to_datetime(gdf['MONTH'], format='%b-%y')

    # print(gdf.head())

    gdf.set_index('MONTH', inplace=True)

    # print(gdf.head())

    # print(df.columns)

    df_prophet = df.reset_index()
    df_prophet = df_prophet.rename(columns={"AVG DAILY(kwh)": "y", "DATE": "ds"})

    print(df_prophet.head())

    df_prophet['floor'] = df_prophet['y'].min() * 0.8
    df_prophet['cap'] = df_prophet['y'].max() * 1.2

    model = Prophet(growth='logistic')

    model.fit(df_prophet)

    # Generate future dates for prediction (e.g., next 30 days)
    future = model.make_future_dataframe(periods=30, freq='D')
    future['floor'] = df_prophet['y'].min() * 0.8
    future['cap'] = df_prophet['y'].max() * 1.2

    # Predict consumption
    forecast = model.predict(future)
    #
    # fig = model.plot(forecast)
    # plt.show()

    forecast.to_csv("forecast/data/s_predictions.csv", index=False)

    gdf_prophet = gdf.reset_index()
    gdf_prophet = gdf_prophet.rename(columns={"TOTAL CONSUMED": "y", "MONTH": "ds"})

    # print(gdf_prophet.head())

    gdf_prophet['floor'] = gdf_prophet['y'].min() * 0.8
    gdf_prophet['cap'] = gdf_prophet['y'].max() * 1.2

    g_model = Prophet(growth='logistic')

    g_model.fit(gdf_prophet)

    # Generate future dates for prediction (e.g., next 10 months)
    g_future = model.make_future_dataframe(periods=10, freq='ME')
    g_future['floor'] = gdf_prophet['y'].min() * 0.8
    g_future['cap'] = gdf_prophet['y'].max() * 1.2

    # Predict consumption
    g_forecast = model.predict(g_future)

    # g_fig = model.plot(g_forecast)
    # plt.show()

    g_forecast.to_csv("forecast/data/g_predictions.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_prophet['ds'], df_prophet['y'], label="Actual Consumption", color="blue")
    ax.plot(forecast['ds'], forecast['yhat'], label="Predicted Consumption", linestyle="dashed", color="red")
    ax.legend()
    plt.xlabel("Date")
    plt.ylabel("Energy Consumption (kWh)")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    g_fig, g_ax = plt.subplots(figsize=(10, 5))
    g_ax.plot(gdf_prophet['ds'], gdf_prophet['y'], label="Actual Consumption", color="blue")
    g_ax.plot(g_forecast['ds'], g_forecast['yhat'], label="Predicted Consumption", linestyle="dashed", color="red")
    g_ax.legend()
    plt.xlabel("Date")
    plt.ylabel("Energy Consumption (kWh)")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    g_image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "forecast.html", {"chart": image_base64, "chart2": g_image_base64})

