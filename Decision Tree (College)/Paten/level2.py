import pandas as pd
import hitungLabel
import gini

data = pd.read_csv("Paten\dbsample.csv")

def parent(rule):
  filter = rule
  where = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(where, 0)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d

  giniD = 1 - (unacc/len(where))**2 - (acc/len(where))**2 - (good/len(where))**2 - (vgood/len(where))**2

  print(
    "\nunacc -->", unacc,
    "\nacc -->", acc,
    "\ngood -->", good,
    "\nvgood -->", vgood
  )
  
  return giniD

def impurity(column, row1, row2, rule):
  if(row2 == 0):
    filter = (data[column]==row1) & rule
    where = data.loc[filter, "Evaluation"].tolist()
    hasil = gini.giniIndex(where, 0)
  else:
    filter = (data[column]==row1) & rule
    where = data.loc[filter, "Evaluation"].tolist()

    filter = (data[column]==row2) & rule
    where2 = data.loc[filter, "Evaluation"].tolist()

    hasil = gini.giniIndex(where, where2)
  
  return hasil

def median(array, column, row1, row2, row3, rule):
  filter = (data[column]==row1) & rule
  where = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(where, 0)
  total = hitungLabel.total

  filter = (data[column]==row2) & rule
  where2 = data.loc[filter, "Evaluation"].tolist()

  filter = (data[column]==row3) & rule
  where3 = data.loc[filter, "Evaluation"].tolist()

  hitungLabel.hitungLabel(where2, where3)
  total2 = hitungLabel.total

  hasil = (total/(total+total2))*array[0] + (total2/(total+total2))*array[1]

  return hasil