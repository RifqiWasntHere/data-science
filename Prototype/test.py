import pandas as pd

df = pd.read_csv("Prototype\dbsample.csv")
filt = (df['Buying'] == 'Low') & ((df['Safety'] == 'Med') | (df['Safety'] == 'High'))
print(df.loc[filt])
