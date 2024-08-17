

# Assuming we have new data for prediction
new_data = pd.DataFrame({
    'Open': [1500.0],
    'High': [1515.0],
    'Low': [1495.0],
    'Close': [1505.0],
    'Volume': [1000000]
})

# Scaling the new data
new_data_scaled = scaler.transform(new_data)

# Predicting the trend
predicted_trend = model.predict(new_data_scaled)

# Convert the prediction back to the original trend label
reverse_trend_mapping = {v: k for k, v in trend_mapping.items()}
print(f"Predicted Trend: {reverse_trend_mapping[predicted_trend[0]]}")
