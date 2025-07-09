import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta

# Load dataset
df = pd.read_csv('sales_data.csv')

# 1. Data Preprocessing

# Parse dates and drop rows with missing essential fields
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date', 'revenue'])

# Optional: Fill missing values in quantity/product if needed
df['quantity'] = df['quantity'].fillna(0)
df['product'] = df['product'].fillna('Unknown')

# Convert date to ordinal
df = df.sort_values('date')
df['date_ordinal'] = df['date'].map(datetime.toordinal)

# X: date as numeric feature
X = df[['date_ordinal']]
y = df['revenue']

# 3. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Training

model = LinearRegression()
model.fit(X_train, y_train)


# 5. Prediction & Evaluation

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"\n Mean Squared Error: {mse:.2f}")


# 6. Future Forecast (Next 10 Days)

last_date = df['date'].max()
future_dates = [last_date + timedelta(days=i) for i in range(1, 11)]
future_ordinals = [d.toordinal() for d in future_dates]

future_df = pd.DataFrame({
    'date': future_dates,
    'date_ordinal': future_ordinals
})
future_df['predicted_revenue'] = model.predict(future_df[['date_ordinal']])

# 7. Plot Results

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['revenue'], label='Actual Sales', marker='o')
plt.plot(future_df['date'], future_df['predicted_revenue'], label='Forecasted Sales', linestyle='--', marker='x')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.title('Actual vs Forecasted Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_forecast_plot.png')  # Optional: Save plot
plt.show()

print("\n Forecast Table (Next 10 Days):")
print(future_df[['date', 'predicted_revenue']].to_string(index=False))
