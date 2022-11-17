import pandas as pd
import hitungGini
from decimal import *
import hitungLabel

data = pd.read_csv("dbsample.csv")     
filter = data["Buying"]=="Low"
low = data.loc[filter, "Evaluation"].tolist()

print(hitungGini.giniIndex(low))