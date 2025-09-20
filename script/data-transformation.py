import pandas as pd

df = pd.read_csv('cleaned_data.csv')
df['age'] = df['age'] / 100  # Simple normalization: divide by 100
