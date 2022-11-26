import pandas as pd
from ginis import parent, impurity, median
import hitungLabel
import tree

data = pd.read_csv("dbsample.csv")

###Iterasi Pertama###
print("\n", "="*10,"Iterasi Pertama", "="*10)
#
#List/Array Gini atribut

Buying =[]
Maintenance = []
Doors = []
Person = []
Lugage_boot = []
Safety = [impurity("Safety", "Low", 0, 0),impurity("Safety", "Med", "Safety", "High")]
#
median = median(Safety, "Safety", "Low", "Med", "High")
#
parent = parent()
#Mencetak Hasil Perhitungan Iterasi Pertama
print(
  "Gini Parent :",
  parent,
)
print(
  "\nImpurity Lugage_boot \\ Small -->",
  "\nImpurity Lugage_boot \\ MedBig -->",
  "\nMedian Gini Lugage_boot -->",
  "\nGain Lugage -->", 

  "\n\nImpurity Safety \\ Low -->", Safety[0],
  "\nImpurity Safety \\ MedHigh -->", Safety[1],
  "\nMedian Gini Safety -->", median,
  "\nGain Safety -->", parent - median,
  "\n\nDecision tree :",
  tree.iterasi1
  )
#
#Struktur decision tree
# tree.iterasi1()
#
#
# filter = data['Buying']=="Low"
# hasil1 = data.loc[filter, "Evaluation"].tolist()
# gini = hitungGini.giniIndex(hasil1, 0)
# print(gini)