import pandas as pd
import hitungLabel
import gini

data = pd.read_csv("Paten\dbsample.csv")

def impurity(column, row1, row2):
  if(row2 == 0):
    filter = data[column]==row1
    where = data.loc[filter, "Evaluation"].tolist()
    hasil = gini.giniIndex(where, 0)
  else:
    filter = data[column]==row1
    where = data.loc[filter, "Evaluation"].tolist()

    filter = data[column]==row2
    where2 = data.loc[filter, "Evaluation"].tolist()

    hasil = gini.giniIndex(where, where2)
  
  return hasil

def median(array, column, row1, row2, row3):
  filter = data[column]==row1
  where = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(where,0)
  total = hitungLabel.total

  filter = data[column]==row2
  where2 = data.loc[filter, "Evaluation"].tolist()

  filter = data[column]==row3
  where3 = data.loc[filter, "Evaluation"].tolist()

  hitungLabel.hitungLabel(where2, where3)
  total2 = hitungLabel.total

  hasil = (total/(total+total2))*array[0] + (total2/(total+total2))*array[1]

  return hasil