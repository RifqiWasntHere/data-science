import pandas as pd
from decimal import *

data = pd.read_csv("dbsample.csv")     
filter1 = data["Evaluation"].tolist()
filter2 = data["Buying"]=="Low"
list(filter2)
filter3 = data["Buying"]=="Low"
print(filter3)
print(data.loc[filter3, "Evaluation"])