import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

# Load data
data = pd.read_excel('Gold price.xlsx')
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by='Date')

# Create month and quarter columns
data['Month'] = data['Date'].dt.month
data['Quarter'] = data['Date'].dt.quarter

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the background color and other styles
app.layout = html.Div(style={'backgroundColor': '#f0f0f0', 'padding': '10px'}, children=[
    html.H1("Gold Price Analysis and Forecasting", style={'textAlign': 'center', 'color': '#333'}),

    html.Label("Select Forecasting Model:", style={'display': 'block', 'margin': '20px 0 10px 0'}),
    dcc.Dropdown(
        id='model-dropdown',
        options=[
            {'label': 'ARIMA', 'value': 'ARIMA'},
            {'label': 'Holt-Winters', 'value': 'HoltWinters'},
            {'label': 'Prophet', 'value': 'Prophet'}
        ],
        value='HoltWinters',
        style={'width': '50%', 'margin': '0 auto'}
    ),
    
    dcc.Graph(id='time-series-chart'),
    dcc.Graph(id='monthly-boxplot'),
    dcc.Graph(id='quarterly-boxplot')
])

# Callback to update graphs based on dropdown selection
@app.callback(
    [Output('time-series-chart', 'figure'),
     Output('monthly-boxplot', 'figure'),
     Output('quarterly-boxplot', 'figure')],
    Input('model-dropdown', 'value')
)
def update_graph(selected_model):
    if selected_model == 'ARIMA':
        # ARIMA Forecasting Code
        model = ARIMA(data['Price'], order=(5, 1, 0))
        model_fit = model.fit()
        future_steps = 12
        future_forecast = model_fit.forecast(steps=future_steps)
        future_dates = pd.date_range(start=data['Date'].iloc[-1], periods=future_steps + 1, freq='M')[1:]
        forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': future_forecast})
        fig = px.line(data, x='Date', y='Price', title='Gold Price Forecast with ARIMA')
        fig.add_scatter(x=forecast_df['Date'], y=forecast_df['Forecast'], mode='lines', name='Forecast')
    
    elif selected_model == 'HoltWinters':
        # Holt-Winters Forecasting Code
        model = ExponentialSmoothing(data['Price'], trend='add', seasonal='add', seasonal_periods=12)
        model_fit = model.fit()
        future_steps = 12
        future_forecast = model_fit.forecast(steps=future_steps)
        future_dates = pd.date_range(start=data['Date'].iloc[-1], periods=future_steps + 1, freq='M')[1:]
        forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': future_forecast})
        fig = px.line(data, x='Date', y='Price', title='Gold Price Forecast with Holt-Winters')
        fig.add_scatter(x=forecast_df['Date'], y=forecast_df['Forecast'], mode='lines', name='Forecast')

    elif selected_model == 'Prophet':
        # Prophet Forecasting Code
        prophet_data = data.rename(columns={'Date': 'ds', 'Price': 'y'})
        model = Prophet()
        model.fit(prophet_data)
        future = model.make_future_dataframe(periods=12, freq='M')
        forecast = model.predict(future)
        forecast_df = forecast[['ds', 'yhat']].rename(columns={'ds': 'Date', 'yhat': 'Forecast'})
        fig = px.line(data, x='Date', y='Price', title='Gold Price Forecast with Prophet')
        fig.add_scatter(x=forecast_df['Date'], y=forecast_df['Forecast'], mode='lines', name='Forecast')

    # Monthly box plot
    monthly_fig = px.box(data, x='Month', y='Price', title='Gold Prices by Month')

    # Quarterly box plot
    quarterly_fig = px.box(data, x='Quarter', y='Price', title='Gold Prices by Quarter')

    return fig, monthly_fig, quarterly_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
