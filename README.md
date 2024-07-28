# Gold Price Analysis and Forecasting

## Objective

The objective of this project is to conduct a comprehensive analysis of gold prices using historical data to understand trends, identify correlations with economic indicators, and develop accurate forecasting models. This project aims to provide valuable insights into the factors influencing gold prices and offer predictive capabilities to assist investors and financial analysts in making informed decisions. By leveraging advanced data analysis techniques, robust visualizations, and time series forecasting models, the project will deliver a detailed understanding of gold price movements and future trends.

## Table of Contents

- [Objective](#objective)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Time Series Forecasting](#time-series-forecasting)
  - [Holt-Winters](#holt-winters)
  - [ARIMA](#arima)
  - [Prophet](#prophet)
  - [Simple Exponential Smoothing](#simple-exponential-smoothing)
  - [Holt’s Linear Trend](#holts-linear-trend)
  - [SARIMA](#sarima)
- [Future Forecasting and Visualization](#future-forecasting-and-visualization)
- [Interactive Dashboard](#interactive-dashboard)
- [Conclusion](#conclusion)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [Results](#results)
- [Author](#author)

## Dataset

The dataset used for this project contains historical gold prices. The dataset includes the following columns:

- `Date`: The date of the gold price record.
- `Price`: The gold price on that date.

## Exploratory Data Analysis (EDA)

The EDA involves the following visualizations:

1. **Line Chart of Gold Prices Over Time**: Shows the trend of gold prices over the entire period.
2. **Moving Average Chart**: Smooths out short-term fluctuations and highlights longer-term trends.
3. **Seasonal Decomposition**: Decomposes the time series into trend, seasonal, and residual components.
4. **Histogram of Gold Prices**: Displays the distribution of gold prices.
5. **Box Plot of Gold Prices by Year**: Identifies outliers and the spread of gold prices each year.
6. **Heatmap of Monthly Average Prices**: Shows the average gold price for each month across multiple years.
7. **Scatter Plot of Gold Prices vs. Year**: Visualizes the relationship between gold prices and the year.
8. **Autocorrelation Plot**: Shows the correlation of the gold prices with a lag of themselves.
9. **Lag Plot**: Visualizes the relationship between gold prices at different time lags.
10. **Box Plot of Gold Prices by Month and Quarter**: Displays the distribution and spread of gold prices by month and quarter.

## Time Series Forecasting

### Holt-Winters

The Holt-Winters method takes into account level, trend, and seasonality for forecasting.

### ARIMA

The ARIMA model is used to forecast the time series based on its own past values.

### Prophet

Prophet is a robust forecasting procedure for time series data that can handle missing data and shifts in the trend.

### Simple Exponential Smoothing

This method is useful for forecasting data with no trend or seasonality.

### Holt’s Linear Trend

This method accounts for a linear trend in the data.

### SARIMA

SARIMA is an extension of ARIMA that supports univariate time series data with a seasonal component.

## Future Forecasting and Visualization

Using the selected forecasting models to predict future gold prices and visualize the results.

## Interactive Dashboard

An interactive dashboard was created using Plotly Dash, providing a user-friendly interface to explore historical data and future forecasts.

## Conclusion

In conclusion, the Gold Price Analysis and Forecasting project provided significant insights into the behavior of gold prices over time. Through extensive exploratory data analysis, various trends and seasonal patterns were identified, offering a deeper understanding of the factors influencing gold prices. The application of multiple time series forecasting models demonstrated varying degrees of accuracy in predicting future gold prices. Among these models, Prophet emerged as the most accurate, making it a reliable tool for forecasting. The interactive dashboard created using Dash provides a user-friendly interface for stakeholders to visualize historical data and future forecasts, enabling better decision-making. Overall, this project underscores the importance of data-driven approaches in financial analysis and offers valuable tools for investors and analysts to navigate the complexities of gold price fluctuations.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gold-price-analysis.git
    cd gold-price-analysis
    ```
2. Run the Jupyter notebook to see the analysis and forecasting:
    ```bash
    jupyter notebook Gold_Price_Analysis_and_Forecasting.ipynb
    ```
3. To run the interactive dashboard, execute the following command:
    ```bash
    python app.py
    ```

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- scikit-learn
- plotly
- dash
- prophet

## Results

| Model                        | MAE          | RMSE         |
|------------------------------|--------------|--------------|
| Holt-Winters                 | 3928.084504  | 5315.362667  |
| ARIMA                        | 6515.481799  | 9076.264036  |
| Prophet                      | 2820.629421  | 3721.573783  |
| Simple Exponential Smoothing | 7455.953351  | 9947.262903  |
| Holt’s Linear Trend          | 3878.912676  | 5265.924687  |
| SARIMA                       | 3305.380067  | 4036.064954  |

## Author

- **Kritika Bhardwaj**
