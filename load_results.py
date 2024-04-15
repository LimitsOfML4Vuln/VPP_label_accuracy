import pandas as pd

df = pd.read_json('./label_accuracy_analysis.json')

print(df.head())
print(df.shape[0])
print(df['label'].value_counts())