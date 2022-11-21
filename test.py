import pandas as pd
import hitungGini

data = pd.read_csv("dbsample.csv")

filter = data["Safety"]=="Med"
small = (data.loc[filter, "Lugage_boot"]=="Small").tolist()
filter = data["Safety"]=="Med"
label = data.loc[filter, "Evaluation"].tolist()



# gini = hitungGini.giniIndex(hasil1)
print(hasil1, "\n", hasil2)

def hitungLugage(arrayName1, arrayName2):
  global a, b, c, total
  a, b, c, d = 0, 0, 0, 0
  a2, b2, c2, d2 = 0, 0, 0, 0
  a3, b3, c3, d3 = 0, 0, 0, 0

  for i in range(len(arrayName2)):
    if(arrayName1[i] == True):
      if ( arrayName2[i] == "unacc"):
        a += 1
      elif ( arrayName2[i] == "acc"):
        b += 1
      elif ( arrayName2[i] == "good"):
        c += 1
      elif ( arrayName2[i] == "vgood"):
        d += 1

  total = a + b + c + d

hitungLugage(hasil1, hasil2)
print(total)