import pandas as pd
import hitungLabel

data = pd.read_csv("dbsample.csv")

def parent():

  evaluation = data["Evaluation"].tolist()

  hitungLabel.hitungLabel(evaluation, 0)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d

  giniD = 1 - (unacc/len(evaluation))**2 - (acc/len(evaluation))**2 - (good/len(evaluation))**2 - (vgood/len(evaluation))**2

  print(
    "\nunacc -->", unacc,
    "\nacc -->", acc,
    "\ngood -->", good,
    "\nvgood -->", vgood
  )

  return giniD

def giniIndex(variable1, variable2):
  global total
  
  if (variable2==0):
    hitungLabel.hitungLabel(variable1, 0)

    unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
    total = hitungLabel.total

  else:
    hitungLabel.hitungLabel(variable1, variable2)

    unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
    total = hitungLabel.total

  if ( total==0 ):
    giniDex = 0
  else:
    giniDex = 1 - (unacc/total)**2 - (acc/total)**2 - (good/total)**2 - (vgood/total)**2
  
  return giniDex

def impurity(column1, row1, column2, row2):
  if(column2 == 0):
    filter = data[column1]==row1
    where = data.loc[filter, "Evaluation"].tolist()
    gini = giniIndex(where, 0)
  else:
    filter = data[column1]==row1
    where = data.loc[filter, "Evaluation"].tolist()

    filter = data[column2]==row2
    where2 = data.loc[filter, "Evaluation"].tolist()

    gini = giniIndex(where, where2)
  
  return gini

def median(array, column, row1, row2, row3):
  filter = data[column]==row1
  where = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(where,0)
  total = hitungLabel.total

  filter = data[column]==row1
  where2 = data.loc[filter, "Evaluation"].tolist()

  filter = data[column]==row2
  where3 = data.loc[filter, "Evaluation"].tolist()

  hitungLabel.hitungLabel(where2, where3)
  total2 = hitungLabel.total

  hasil = (total/(total+total2))*array[0] + (total2/(total+total2))*array[1]

  return hasil