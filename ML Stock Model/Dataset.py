

# Load the dataset

data = pd.read_csv('stock_data.csv')

print(data.head())

trend_mapping = {
    'Up': 1,
    'Down': 0
}

data['Trend'] = data['Trend'].map(trend_mapping)
