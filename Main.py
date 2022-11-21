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

def hitungDuaLabelRow(column1, row1, column2, row2):
  filter = data[column1]==row1
  hasil = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(hasil)
  total1 = hitungLabel.total

  filter = data[column2]==row2
  hasil = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(hasil)
  total2 = hitungLabel.total + total1

  return total2

def hitungMedianGini(column):
  median = (column[3]/16)*column[0] + (column[4]/16)*0.69421
  
  return median

def hitungGain(median):
  gini = 0.71875
  gain =  gini - median

  return gain

print("\n", "="*10,"Iterasi Pertama", "="*10)
#List/Array Gini atribut
Buying = [hitungImpurity("Buying", "Low"), hitungImpurity("Buying", "Med"),  hitungImpurity("Buying", "High"), hitungLabelRow("Buying", "Low"), hitungLabelRow("Buying", "Med"),  hitungLabelRow("Buying", "High")]
Maintenance = [hitungImpurity("Maintenance", "Low"), hitungImpurity("Maintenance", "Med"), hitungImpurity("Maintenance", "High"), hitungLabelRow("Maintenance", "Low"), hitungLabelRow("Maintenance", "Med"), hitungLabelRow("Maintenance", "High")]
Doors = [hitungImpurity("Doors", "3"), hitungImpurity("Doors", "4"), hitungImpurity("Doors", "More"), hitungLabelRow("Doors", "3"), hitungLabelRow("Doors", "4"), hitungLabelRow("Doors", "More")]
Person = [hitungImpurity("Person", "2"), hitungImpurity("Person", "4"), hitungImpurity("Person", "More"), hitungLabelRow("Person", "2"), hitungLabelRow("Person", "4"), hitungLabelRow("Person", "More")]
Lugage_boot = [hitungImpurity("Lugage_boot", "Small"), hitungImpurity("Lugage_boot", "Med"), hitungImpurity("Lugage_boot", "Big"), hitungLabelRow("Lugage_boot", "Small"), hitungLabelRow("Lugage_boot", "Med"), hitungLabelRow("Lugage_boot", "Big")]
Safety = [hitungImpurity("Safety", "Low"), hitungImpurity("Safety", "Med"), hitungImpurity("Safety", "High"), hitungLabelRow("Safety", "Low"), hitungDuaLabelRow("Safety", "Med", "Safety", "High")]

print(
  # "Impurity Buying \\ Low -->", Buying[0],
  # "\nImpurity Buying \\ MedHigh -->", (Buying[1] + Buying[2])/2,
  # "\nMedian Gini Buying -->", hitungMedianGini(Buying),
  # "\nGain Buying -->", hitungGain(hitungMedianGini(Buying)),

  # "\n\nImpurity Maintenance \\ Low -->", Maintenance[0],
  # "\nImpurity Maintenance \\ MedHigh -->", (Maintenance[1] + Maintenance[2])/2,
  # "\nMedian Gini Maintenance -->", hitungMedianGini(Maintenance),
  # "\nGain Maintenance -->", hitungGain(hitungMedianGini(Maintenance)),

  # "\n\nImpurity Doors \\ 3 -->", Doors[0],
  # "\nImpurity Doors \\ 4More -->", (Doors[1] + Doors[2])/2,
  # "\nMedian Gini Doors -->", hitungMedianGini(Doors),
  # "\nGain Doors -->", hitungGain(hitungMedianGini(Doors)),

  # "\n\nImpurity Person \\ 2 -->", Person[0],
  # "\nImpurity Person \\ 4More -->", (Person[1] + Person[2])/2,
  # "\nMedian Gini Person -->", hitungMedianGini(Person),
  # "\nGain Person -->", hitungGain(hitungMedianGini(Person)), 

  "\n\nImpurity Lugage_boot \\ Small -->", Lugage_boot[0],
  "\nImpurity Lugage_boot \\ MedBig -->", (Lugage_boot[1] + Lugage_boot[2])/2,
  "\nMedian Gini Lugage_boot -->", hitungMedianGini(Lugage_boot),
  "\nGain Lugage -->", hitungGain(hitungMedianGini(Lugage_boot)), 

  "\n\nImpurity Safety \\ Low -->", Safety[0],
  "\nImpurity Safety \\ MedHigh -->", (Safety[1] + Safety[2])/2,
  "\nMedian Gini Safety -->", hitungMedianGini(Safety),
  "\nGain Safety -->", hitungGain(hitungMedianGini(Safety)),
  )

# Validasi data Safety Med & High
# print("Safety||Med -->", (hitungImpurity("Safety", "Med"),"\nSafety||High -->",hitungImpurity("Safety", "High")))
# print("\n", "="*10,"Iterasi Kedua", "="*10)

# filter = data["Safety"]=="Low"

# print("\nData Safety yang bernilai low : ")
# print(data.loc[filter, "Evaluation"].tolist())

# print("\n", "="*10,"Iterasi Ketiga", "="*10)
