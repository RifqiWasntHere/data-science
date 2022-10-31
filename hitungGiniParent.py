from tokenize import String
import pandas as pd


def giniParent(csvFile):
  
  cari = pd.read_csv("dbsample.csv") 
  evaluation = cari["Evaluation"].tolist()

  unacc, acc, good, vgood = 0, 0, 0, 0

  for i in range(len(evaluation)):
    if ( evaluation[i] == "unacc" ):
      unacc += 1
    elif ( evaluation[i] == "acc" ):
      acc += 1
    elif ( evaluation[i] == "good" ):
      good += 1
    elif ( evaluation[i] == "vgood" ):
      vgood += 1

  # print(
  #   unacc,
  #   acc,
  #   good,
  #   vgood
  # )

  giniD = 1 - (unacc/len(evaluation))**2 - (acc/len(evaluation))**2 - (good/len(evaluation))**2 - (vgood/len(evaluation))**2
  return giniD