import pandas as pd

# Load individual sample files
samples = ['sample_2020.csv', 'sample_2021.csv', 'sample_2022.csv']
dataframes = [pd.read_csv(file) for file in samples]

# Combine into one dataframe
combined_data = pd.concat(dataframes)

# Save combined data
combined_data.to_csv('data/processed_data/combined_data.csv', index=False)
print("Combined data saved to 'combined_data.csv'")
