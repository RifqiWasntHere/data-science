import pandas as pd
import hitungGini
from decimal import *
import hitungLabel
data = pd.read_csv("dbsample.csv") 

def hitungImpurity(column, row):
  filter = data[column]==row
  hasil = data.loc[filter, "Evaluation"].tolist()
  # print("Impurity", row, "-->", hitungGini.giniIndex(hasil))
  gini = hitungGini.giniIndex(hasil)
  
  return gini

def hitungLabelRow(column, row):
  filter = data[column]==row
  hasil = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(hasil)
  total = hitungLabel.total
  
  return total

def hitungMedianGini(column):
  median = (column[3]/16)*column[0] + (column[4]+column[5]/16)*(column[1]+column[2])
  
  return median

#List/Array Gini atribut
Buying = [hitungImpurity("Buying", "Low"), hitungImpurity("Buying", "Med"),  hitungImpurity("Buying", "High"), hitungLabelRow("Buying", "Low"), hitungLabelRow("Buying", "Med"),  hitungLabelRow("Buying", "High")]
Maintenance = [hitungImpurity("Maintenance", "Low"), hitungImpurity("Maintenance", "Med"), hitungImpurity("Maintenance", "High"), hitungLabelRow("Maintenance", "Low"), hitungLabelRow("Maintenance", "Med"), hitungLabelRow("Maintenance", "High")]
Doors = [hitungImpurity("Doors", "3"), hitungImpurity("Doors", "4"), hitungImpurity("Doors", "More"), hitungLabelRow("Doors", "3"), hitungLabelRow("Doors", "4"), hitungLabelRow("Doors", "More")]
Person = [hitungImpurity("Person", "2"), hitungImpurity("Person", "4"), hitungImpurity("Person", "More"), hitungLabelRow("Person", "2"), hitungLabelRow("Person", "4"), hitungLabelRow("Person", "More")]
Lugage_boot = [hitungImpurity("Lugage_boot", "Small"), hitungImpurity("Lugage_boot", "Med"), hitungImpurity("Lugage_boot", "Big"), hitungLabelRow("Lugage_boot", "Small"), hitungLabelRow("Lugage_boot", "Med"), hitungLabelRow("Lugage_boot", "Big")]
Safety = [hitungImpurity("Safety", "Low"), hitungImpurity("Safety", "Med"), hitungImpurity("Safety", "High"), hitungLabelRow("Safety", "Low"), hitungLabelRow("Safety", "Med"), hitungLabelRow("Safety", "High")]

print(
  "Impurity Buying \\ Low -->", Buying[0],
  "\nImpurity Buying \\ MedHigh -->", Buying[1] + Buying[2],
  "\nMedian Gini Buying -->", hitungMedianGini(Buying),

  "\n\nImpurity Maintenance \\ Low -->", Maintenance[0],
  "\nImpurity Maintenance \\ MedHigh -->", Maintenance[1] + Maintenance[2],
  "\nMedian Gini Maintenance -->", hitungMedianGini(Maintenance),

  "\n\nImpurity Doors \\ 3 -->", Doors[0],
  "\nImpurity Doors \\ 4More -->", Doors[1] + Doors[2],
  "\nMedian Gini Doors -->", hitungMedianGini(Doors),

  "\n\nImpurity Person \\ 2 -->", Person[0],
  "\nImpurity Person \\ 4More -->", Person[1] + Person[2],
  "\nMedian Gini Person -->", hitungMedianGini(Person),

  "\n\nImpurity Lugage_boot \\ Small -->", Lugage_boot[0],
  "\nImpurity Lugage_boot \\ MedBig -->", Lugage_boot[1] + Lugage_boot[2],
   "\nMedian Gini Lugage_boot -->", hitungMedianGini(Lugage_boot),

  "\n\nImpurity Safety \\ Low -->", Safety[0],
  "\nImpurity Safety \\ MedHigh -->", Safety[1] + Safety[2],
    "\nMedian Gini Safety -->", hitungMedianGini(Safety),

  )

