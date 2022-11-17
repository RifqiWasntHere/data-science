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

  hitungLabel.hitungLabel(variable)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d

  giniDex = 1 - (unacc/len(variable))**2 - (acc/len(variable))**2 - (good/len(variable))**2 - (vgood/len(variable))**2
  return giniDex