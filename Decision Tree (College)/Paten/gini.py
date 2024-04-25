import pandas as pd
import hitungLabel

data = pd.read_csv("Paten\dbsample.csv")

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