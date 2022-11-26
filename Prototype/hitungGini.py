import pandas as pd
import hitungLabel

def parent(csvFile):

  cari = pd.read_csv(csvFile) 
  evaluation = cari["Evaluation"].tolist()

  hitungLabel.hitungLabel(evaluation)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d

  giniD = 1 - (unacc/len(evaluation))**2 - (acc/len(evaluation))**2 - (good/len(evaluation))**2 - (vgood/len(evaluation))**2
  return giniD

def giniIndex(variable):
  global total

  hitungLabel.hitungLabel(variable, 0)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
  total = hitungLabel.total

  giniDex = 1 - (unacc/total)**2 - (acc/total)**2 - (good/total)**2 - (vgood/total)**2
  
  if ( total==0 ):
    giniDex = 0
  
  return giniDex

def giniIndex2(variable1, variable2):
  global total

  hitungLabel.hitungLabel(variable1, variable2)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
  total = hitungLabel.total

  if ( total==0 ):
    giniDex = 0
  else:
    giniDex = 1 - (unacc/total)**2 - (acc/total)**2 - (good/total)**2 - (vgood/total)**2
  
  return giniDex

def giniAtribut(column1, row1, column2, row2):
  
  data = pd.read_csv("dbsample.csv")

  filter = ( data[column1] == row1 ) & ( data[column2] == row2 )
  filtered = data.loc[filter, "Evaluation"].tolist()

  hitungLabel.hitungLabel(filtered, 0)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
  total = hitungLabel.total
  
  print("Record pada", column2, row2, "->", unacc, acc, good, vgood)

  if ( total==0 ):
    giniDex = 0
  else:
    giniDex = 1 - (unacc/total)**2 - (acc/total)**2 - (good/total)**2 - (vgood/total)**2

  return giniDex