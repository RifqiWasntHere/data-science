import pandas as pd

data = pd.read_csv("Paten\dbsample.csv")
columns = ["Buying","Maintenance","Doors","Person","Lugage_boot","Safety"]

def iterasi1():
  from gini import parent
  from level1 import impurity, median
  import tree
  ###Iterasi Pertama###
  print("\n", "="*10,"Iterasi Pertama", "="*10)
  #
  #List/Array Gini atribut
  Buying =[impurity("Buying", "Low", 0, 0),impurity("Buying", "Med", "Buying", "High")]
  Maintenance = [impurity("Maintenance", "Low", 0, 0),impurity("Maintenance", "Med", "Maintenance", "High")]
  Doors = [impurity("Doors", "3", 0, 0),impurity("Doors", "4", "Doors", "More")]
  Person = [impurity("Person", "2", 0, 0),impurity("Person", "4", "Person", "More")]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0, 0),impurity("Lugage_boot", "Med", "Lugage_boot", "Big")]
  Safety = [impurity("Safety", "Low", 0, 0),impurity("Safety", "Med", "Safety", "High")]
  #
  parent = parent()
  #
  median = [
            median(Buying, "Buying", "Low", "Med", "High"),median(Maintenance, "Maintenance", "Low", "Med", "High"),
            median(Doors, "Doors", "3", "4", "More"),median(Person, "Person", "2", "4", "More"),
            median(Lugage_boot, "Lugage_boot", "Small", "Med", "Big"),median(Safety, "Safety", "Low", "Med", "High")
            ]
  #
  gain = [
          parent-median[0], parent-median[1], parent-median[2],
          parent-median[3], parent-median[4], parent-median[5]
        ]
  #Mencetak Hasil Perhitungan Iterasi Pertama
  print(
    "Gini Parent :",
    parent,
  )
  print(
    "\nImpurity Buying \\ Low -->", Buying[0],
    "\nImpurity Buying \\ MedHigh -->", Buying[1],
    "\nMedian Gini Buying -->", median[0],
    "\nGain Buying -->", gain[0],

    "\n\nImpurity Maintenance \\ Low -->", Maintenance[0],
    "\nImpurity Maintenance \\ MedHigh -->", Maintenance[1],
    "\nMedian Gini Maintenance -->", median[1],
    "\nGain Maintenance -->", gain[1],

    "\n\nImpurity Doors \\ 3 -->", Doors[0],
    "\nImpurity Doors \\ 4More -->", Doors[1],
    "\nMedian Gini Doors -->", median[2],
    "\nGain Doors -->", gain[2],
    
    "\n\nImpurity Person \\ 2 -->", Person[0],
    "\nImpurity Person \\ 4More -->", Person[1],
    "\nMedian Gini Person -->", median[3],
    "\nGain Person -->", gain[3],

    "\n\nImpurity Lugage_boot \\ Small -->", Lugage_boot[0],
    "\nImpurity Lugage_boot \\ MedBig -->", Lugage_boot[1],
    "\nMedian Gini Lugage_boot -->", median[4],
    "\nGain Lugage_boot -->", gain[4],

    "\n\nImpurity Safety \\ Low -->", Safety[0],
    "\nImpurity Safety \\ MedHigh -->", Safety[1],
    "\nMedian Gini Safety -->", median[5],
    "\nGain Safety -->", gain[5],

    "\n\nGain terbesar :", columns[gain.index(max(gain))],

    "\n\nDecision tree :"
    )
  #
  #Struktur decision tree
  tree.iterasi1()
  #

def iterasi2():
  import tree
  ###Iterasi Kedua###
  print("\n", "="*10,"Iterasi Kedua", "="*10, "\n")
  #
  filter = data["Safety"]=="Low"
  #
  print("Dataset yang bernilai Safety == low : \n")
  print(data.loc[filter])
  print(
    "\nDikarenakan dataset memiliki label homogen, \nmaka cabang kiri akan langsung dinyatakan [unacc]"
    )
  #
  print("\nDecision tree :")
  #
  #Struktur decision tree
  tree.iterasi2()

def iterasi3():
  from level2 import parent, impurity, median
  import tree
  ###Iterasi Ketiga###
  print("\n", "="*10,"Iterasi Ketiga", "="*10, "\n")
  #
  #List/Array Gini atribut
  Buying =[impurity("Buying", "Low", 0, 0),impurity("Buying", "Med", "Buying", "High")]
  Maintenance = [impurity("Maintenance", "Low", 0, 0),impurity("Maintenance", "Med", "Maintenance", "High")]
  Doors = [impurity("Doors", "3", 0, 0),impurity("Doors", "4", "Doors", "More")]
  Person = [impurity("Person", "2", 0, 0),impurity("Person", "4", "Person", "More")]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0, 0),impurity("Lugage_boot", "Med", "Lugage_boot", "Big")]
  Safety = [impurity("Safety", "Low", 0, 0),impurity("Safety", "Med", "Safety", "High"), impurity("Safety", "Med", 0, 0), impurity("Safety", "High", 0, 0)]
  #
  parent = parent("Safety", "Med", "High")
  #
  median = [
            median(Buying, "Buying", "Low", "Med", "High"),median(Maintenance, "Maintenance", "Low", "Med", "High"),
            median(Doors, "Doors", "3", "4", "More"),median(Person, "Person", "2", "4", "More"),
            median(Lugage_boot, "Lugage_boot", "Small", "Med", "Big"),median(Safety, "Safety", "Low", "Med", "High")
            ]
  #
  gain = [
          parent-median[0], parent-median[1], parent-median[2],
          parent-median[3], parent-median[4], parent-median[5]
        ]
  #Mencetak Hasil Perhitungan Iterasi Ketiga
  print(
    "Gini Parent :",
    parent,
  )
  print(
    "\nImpurity Buying \\ Low -->", Buying[0],
    "\nImpurity Buying \\ MedHigh -->", Buying[1],
    "\nMedian Gini Buying -->", median[0],
    "\nGain Buying -->", gain[0],

    "\n\nImpurity Maintenance \\ Low -->", Maintenance[0],
    "\nImpurity Maintenance \\ MedHigh -->", Maintenance[1],
    "\nMedian Gini Maintenance -->", median[1],
    "\nGain Maintenance -->", gain[1],

    "\n\nImpurity Doors \\ 3 -->", Doors[0],
    "\nImpurity Doors \\ 4More -->", Doors[1],
    "\nMedian Gini Doors -->", median[2],
    "\nGain Doors -->", gain[2],
    
    "\n\nImpurity Person \\ 2 -->", Person[0],
    "\nImpurity Person \\ 4More -->", Person[1],
    "\nMedian Gini Person -->", median[3],
    "\nGain Person -->", gain[3],

    "\n\nImpurity Lugage_boot \\ Small -->", Lugage_boot[0],
    "\nImpurity Lugage_boot \\ MedBig -->", Lugage_boot[1],
    "\nMedian Gini Lugage_boot -->", median[4],
    "\nGain Lugage_boot -->", gain[4],

    "\n\nImpurity Safety \\ Low -->", Safety[0],
    "\nImpurity Safety \\ MedHigh -->", Safety[1],
    "\nMedian Gini Safety -->", median[5],
    "\nGain Safety -->", gain[5],

    "\n\nGain terbesar :", columns[gain.index(max(gain))],

    "\nSafety Med vs High : "
    "\nImpurity Safety \\ Med -->", Safety[2],
    "\nImpurity Safety \\ High -->", Safety[2],
    
    "\n\nSafety akan dijadikan sebagai parent untuk node selanjutnya,"
    "\nDikarenakan impurity Safety adalah yang paling besar diantara semua atribut"
    "\n\nDecision tree :"
    )
  #
  #Struktur decision tree
  tree.iterasi3()
  #