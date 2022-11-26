import pandas as pd

df = pd.read_csv("dbsample.csv")
filt = (df['Safety'] == 'Med') & (df['Safety'] == 'High')
print(df.loc[filt])
