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

  hitungLabel.hitungLabel(variable)

  unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
  total = hitungLabel.total

  if ( total == 0 ):
    giniDex = 0
  else:
    giniDex = 1 - (unacc/total)**2 - (acc/total)**2 - (good/total)**2 - (vgood/total)**2
  
  return giniDex

data = pd.read_csv("dbsample.csv")
filter = data["Safety"]=="Med"
hasil = data.loc[filter, "Evaluation"].tolist()


data = pd.read_csv("dbsample.csv")
filter = data["Safety"]=="High"
hasil2 = data.loc[filter, "Evaluation"].tolist()
hitungLabel.hitungLabel(hasil, hasil2)
unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
total = hitungLabel.total

print(total)
print(unacc,acc,good,vgood)
print(total/total-(unacc/total)**2-(acc/total)**2-(good/total)**2-(vgood/total)**2)



# unacc2, acc2, good2, vgood2 = hitungLabel.a+unacc, hitungLabel.b+acc, hitungLabel.c+good, hitungLabel.d+vgood
# total2 = hitungLabel.total+total
# print(total2)

# print(1 - (unacc2/total2)**2 - (acc2/total2)**2 - (good2/total2)**2 - (vgood2/total2)**2)
