import pandas as pd
from treelib import Tree
from decimal import *
import hitungGini
import hitungLabel
import tree

data = pd.read_csv("dbsample.csv") 

def hitungImpurity(column1, row1, column2, row2):
  if(column2 == 0):
    filter = data[column1]==row1
    hasil1 = data.loc[filter, "Evaluation"].tolist()
    gini = hitungGini.giniIndex(hasil1)
  else:
    filter = data[column1]==row1
    hasil1 = data.loc[filter, "Evaluation"].tolist()

    filter = data[column2]==row2
    hasil2 = data.loc[filter, "Evaluation"].tolist()
    gini = hitungGini.giniIndex2(hasil1, hasil2)
  
  return gini

def hitungLabelRow(column, row):
  filter = data[column]==row
  hasil = data.loc[filter, "Evaluation"].tolist()
  hitungLabel.hitungLabel(hasil,0)
  total = hitungLabel.total
  
  return total

def hitungDuaLabelRow(column1, row1, column2, row2):
  filter = data[column1]==row1
  hasil1 = data.loc[filter, "Evaluation"].tolist()

  filter = data[column2]==row2
  hasil2 = data.loc[filter, "Evaluation"].tolist()

  hitungLabel.hitungLabel(hasil1, hasil2)
  total = hitungLabel.total

  return total

def hitungMedianGini(column, total):
  median = (column[2]/total)*column[0] + (column[3]/total)*column[1]
  
  return median

def hitungGain(median):
  gini = 0.71875
  gain =  gini - median

  return gain

###Iterasi Pertama###
print("\n", "="*10,"Iterasi Pertama", "="*10)
#
#List/Array Gini atribut
Lugage_boot = [hitungImpurity("Lugage_boot", "Small", 0, 0), hitungImpurity("Lugage_boot", "Med", "Lugage_boot", "Big"), hitungLabelRow("Lugage_boot", "Small"), hitungDuaLabelRow("Lugage_boot", "Med", "Lugage_boot", "Big")]
Safety = [hitungImpurity("Safety", "Low", 0, 0), hitungImpurity("Safety", "Med", "Safety", "High"), hitungLabelRow("Safety", "Low"), hitungDuaLabelRow("Safety", "Med", "Safety", "High")]
#
#Mencetak Hasil Perhitungan Iterasi Pertama
print(
  "\nImpurity Lugage_boot \\ Small -->", Lugage_boot[0],
  "\nImpurity Lugage_boot \\ MedBig -->", Lugage_boot[1],
  "\nMedian Gini Lugage_boot -->", hitungMedianGini(Lugage_boot, 16),
  "\nGain Lugage -->", hitungGain(hitungMedianGini(Lugage_boot, 16)), 

  "\n\nImpurity Safety \\ Low -->", Safety[0],
  "\nImpurity Safety \\ MedHigh -->", Safety[1],
  "\nMedian Gini Safety -->", hitungMedianGini(Safety, 16),
  "\nGain Safety -->", hitungGain(hitungMedianGini(Safety, 16)),
  "\n\nDecision tree :"
  )
#
#Struktur decision tree
tree.iterasi1()
#
#
###Iterasi Kedua###
print("\n", "="*10,"Iterasi Kedua", "="*10, "\n")
#
filter = data["Safety"]=="Low"
#
print("\nData Safety yang bernilai low : ")
print(data.loc[filter, "Evaluation"].tolist())
#
print("\nDecision tree :")
#
#Struktur decision tree
tree.iterasi2()
#
#
print("\n", "="*10,"Iterasi Ketiga", "="*10, "\n")
# Mencari Gain dari Cabang Safety [Med, High] dan menjadikan kandidat
# dengan Gain terbesar sebagai Cabang Kiri
#
parent = hitungImpurity("Safety", "Med", "Safety", "High")
#
#List/Array Gini atribut
Safety = [hitungImpurity("Safety", "Med", 0, 0), hitungImpurity("Safety", "High", 0, 0), hitungLabelRow("Safety", "Med"), hitungLabelRow("Safety", "High")]
#
#Mencetak hasil perhitungan
print(
  "\nImpurity Safety \\ Med -->", Safety[0],
  "\nImpurity Safety \\ High -->", Safety[1],
  "\nMedian Gini Safety -->", hitungMedianGini(Safety, 11),
  "\nGain Safety -->", (parent - hitungMedianGini(Safety, 11)),
  #Dikarenakan Gain Cabang Med > High, maka Cabang Med akan dijadikan
  #sebagai cabang kiri
  "\n\nDecision tree :"
)
#
#Struktur decision tree
tree.iterasi3()


###Iterasi Keempat###
print("\n", "="*10,"Iterasi Keempat", "="*10, "\n")
#
#
#List/Array Gini atribut
Lugage_boot = [hitungGini.giniAtribut("Safety", "Med", "Lugage_boot", "Small"), hitungGini.giniAtribut("Safety", "Med", "Lugage_boot", "Med"), hitungGini.giniAtribut("Safety", "Med", "Lugage_boot", "Big")]
# Safety = [hitungImpurity("Safety", "Low", 0, 0), hitungImpurity("Safety", "Med", "Safety", "High"), hitungLabelRow("Safety", "Low"), hitungDuaLabelRow("Safety", "Med", "Safety", "High")]
#
parent = 1-(1/6)**2-(2/6)**2-(3/6)**2-(0/6)**2
#
medianLugage = (3/6)*Lugage_boot[0] + (3/6)*Lugage_boot[1]
#
#Mencetak Hasil Perhitungan Iterasi Keempat
print(
  "\nImpurity Lugage_boot \\ Small -->", Lugage_boot[0],
  "\nImpurity Lugage_boot \\ MedBig -->", (Lugage_boot[1] + Lugage_boot[2])/2,
  "\nMedian Gini Lugage_boot -->", medianLugage,
  "\nGain Lugage -->", parent - medianLugage, 
#
#Safety tidak dihitung karena sudah menjadi parent dari iterasi keempat
#
  "\n\nImpurity Safety \\ Low -->", 0,
  "\nImpurity Safety \\ MedHigh -->", 0,
  "\nMedian Gini Safety -->", 0,
  "\nGain Safety -->", 0,
#Dikarenakan Gain Cabang Small > MedBig, maka Cabang Small akan dijadikan
#sebagai cabang kiri
  "\n\nDecision tree :"
  )
#
#Struktur decision tree
tree.iterasi4()
#
#
###Iterasi Kelima###
# print("\n", "="*10,"Iterasi Kelima", "="*10)
#
#Dikarenakan pada lugage_boot tidak terdapat data Homogen, maka itu
#label node akan ditentukan dengan nilai Label yang dominan
#
# filter = data["Safety"].tolist()
# filter1 = data["Lugage_boot"].tolist()
# filter2 = data["Evaluation"].tolist()
# print("Data pada Lugage_boot: ") 
# print(filter, filter1, filter2,  "\nLabel yang dominan : ", "\n Tidak ada.")
