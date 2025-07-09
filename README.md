# Save the README content to a readme.txt file

readme_content = """
Sales Forecasting with Linear Regression
========================================

This project demonstrates a simple sales forecasting model using Python libraries like pandas, matplotlib, and scikit-learn.

Overview
--------
- Reads sales data from 'sales_data.csv'
- Handles missing values and converts dates to numerical format
- Trains a Linear Regression model on past sales revenue
- Predicts sales revenue for the next 10 days
- Visualizes actual and forecasted sales

Dataset Format
--------------
Expected columns in sales_data.csv:
- date (e.g., 2024-04-01)
- product (optional)
- quantity (optional)
- revenue (e.g., 1000)

Requirements
------------
- pandas
- matplotlib
- scikit-learn

Install dependencies with:
pip install pandas matplotlib scikit-learn

Running the Script
------------------
Ensure 'sales_data.csv' is in the same folder as the script. Then run:

python forecast.py

Outputs
-------
- Console: Mean Squared Error and forecast table for next 10 days
- PNG Image: 'sales_forecast_plot.png' showing actual vs predicted sales

Screenshot
----------
See 'sales_forecast_plot.png' for the sample visualization.


