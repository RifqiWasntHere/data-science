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
  Buying =[impurity("Buying", "Low", 0),impurity("Buying", "Med", "High")]
  Maintenance = [impurity("Maintenance", "Low", 0),impurity("Maintenance", "Med", "High")]
  Doors = [impurity("Doors", "3", 0),impurity("Doors", "4", "More")]
  Person = [impurity("Person", "2", 0),impurity("Person", "4", "More")]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0),impurity("Lugage_boot", "Med", "Big")]
  Safety = [impurity("Safety", "Low", 0),impurity("Safety", "Med", "High")]
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
    "\nDikarenakan data dari cabang tersebut memiliki label homogen unacc, \nmaka cabang kiri akan langsung dinyatakan sebagai leaf [unacc]"
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
  rule = ((data['Safety'] == 'Med') | (data['Safety'] == 'High'))
  # rule
  #List/Array Gini atribut
  Buying =[impurity("Buying", "Low", 0, rule),impurity("Buying", "Med", "High", rule)]
  Maintenance = [impurity("Maintenance", "Low", 0, rule),impurity("Maintenance", "Med", "High", rule)]
  Doors = [impurity("Doors", "3", 0, rule),impurity("Doors", "4", "More", rule)]
  Person = [impurity("Person", "2", 0, rule),impurity("Person", "4", "More", rule)]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0, rule),impurity("Lugage_boot", "Med", "Big", rule)]
  Safety = [impurity("Safety", "Med", 0, rule),impurity("Safety", "High", 0, rule)]
  #
  parent = parent(rule)
  #
  median = [
            median(Buying, "Buying", "Low", "Med", "High", rule),median(Maintenance, "Maintenance", "Low", "Med", "High", rule),
            median(Doors, "Doors", "3", "4", "More", rule),median(Person, "Person", "2", "4", "More", rule),
            median(Lugage_boot, "Lugage_boot", "Small", "Med", "Big", rule),median(Safety, "Safety", "Low", "Med", "High", rule)
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

    "\n\nImpurity Safety \\ Med -->", Safety[0],
    "\nImpurity Safety \\ High -->", Safety[1],
    "\nMedian Gini Safety -->", median[5],
    "\nGain Safety -->", gain[5],
    ###Catatan : Nilai yang tertera berbeda dengan yang ada di modul
    ###Dikarenakan, Pada cabang anak kiri pada modul, terhitung LowHigh
    ###Yang dimana tidak dapat dilakukan karena record low telah menjadi
    ###Parent dari cabang ini / sudah tereliminasi
    "\n\nGain terbesar :", columns[gain.index(max(gain))],
    
    "\n\nSafety akan dijadikan sebagai parent untuk node selanjutnya,"
    "\nDikarenakan impurity Safety adalah yang paling besar diantara semua atribut"
    "\n\nDecision tree :"
    )
  #
  #Struktur decision tree
  tree.iterasi3()
  #

def iterasi4():
  from level2 import parent, impurity, median
  import tree
  ###Iterasi Keempat###
  print("\n", "="*10,"Iterasi Keempat", "="*10, "\n")
  #
  rule = (data['Safety'] == 'Med')
  #, rule
  #List/Array Gini atribut
  Buying =[impurity("Buying", "Low", 0, rule),impurity("Buying", "Med", "High", rule)]
  Maintenance = [impurity("Maintenance", "Low", 0, rule),impurity("Maintenance", "Med", "High", rule)]
  Doors = [impurity("Doors", "3", 0, rule),impurity("Doors", "4", "More", rule)]
  Person = [impurity("Person", "2", 0, rule),impurity("Person", "4", "More", rule)]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0, rule),impurity("Lugage_boot", "Med", "Big", rule)]
  #
  parent = parent(rule)
  #
  median = [
            median(Buying, "Buying", "Low", "Med", "High", rule),median(Maintenance, "Maintenance", "Low", "Med", "High", rule),
            median(Doors, "Doors", "3", "4", "More", rule),median(Person, "Person", "2", "4", "More", rule),
            median(Lugage_boot, "Lugage_boot", "Small", "Med", "Big", rule)
            ]
  #
  gain = [
          parent-median[0], parent-median[1], parent-median[2],
          parent-median[3], parent-median[4]
        ]
  #Mencetak Hasil Perhitungan Iterasi Keempat
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

    "\n\nGain terbesar :", columns[gain.index(max(gain))],
    
    "\n\nDecision tree :"
    )
  #
  #Struktur decision tree
  tree.iterasi4()
  #

def iterasi5():
  from level2 import parent, impurity, median
  import tree
  ###Iterasi Kelima###
  print("\n", "="*10,"Iterasi Kelima", "="*10)
  #
  rule = ((data['Safety'] == 'Med') & (data['Lugage_boot'] == 'Small'))
  #, rule
  #List/Array Gini atribut
  Buying =[impurity("Buying", "Low", 0, rule),impurity("Buying", "Med", "High", rule)]
  Maintenance = [impurity("Maintenance", "Low", 0, rule),impurity("Maintenance", "Med", "High", rule)]
  Doors = [impurity("Doors", "3", 0, rule),impurity("Doors", "4", "More", rule)]
  Person = [impurity("Person", "2", 0, rule),impurity("Person", "4", "More", rule)]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0, rule),impurity("Lugage_boot", "Med", "Big", rule)]
  #
  parent = parent(rule)
  #
  median = [
            median(Buying, "Buying", "Low", "Med", "High", rule),median(Maintenance, "Maintenance", "Low", "Med", "High", rule),
            median(Doors, "Doors", "3", "4", "More", rule),median(Person, "Person", "2", "4", "More", rule),
            median(Lugage_boot, "Lugage_boot", "Small", "Med", "Big", rule)
            ]
  #
  gain = [
          parent-median[0], parent-median[1], parent-median[2],
          parent-median[3], parent-median[4]
        ]
  #Mencetak Hasil Perhitungan Iterasi Kelima
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

    "\n\nGain terbesar :", columns[gain.index(max(gain))],
    
    "\n\nDecision tree :"
    )
  #
  #Struktur decision tree
  tree.iterasi5()
  #

def iterasi6():
  import tree
  ###Iterasi Keenam###
  print("\n", "="*10,"Iterasi Keenam", "="*10, "\n")
  #
  filter = (data["Safety"]=="Med") & (data["Lugage_boot"]=="Small") & (data["Person"]=="2")
  #
  print("Dataset dari cabang Person [2] : \n")
  print(data.loc[filter])
  print(
    "\nDikarenakan data dari cabang tersebut memiliki label homogen unacc, \nmaka cabang tersebut dinyatakan sebagai leaf[unacc]"
    )
  #
  print("\nDecision tree :")
  #
  #Struktur decision tree
  tree.iterasi6()

def iterasi7():
  import tree
  ###Iterasi Ketujuh###
  print("\n", "="*10,"Iterasi Ketujuh", "="*10, "\n")
  #
  filter = (data["Safety"]=="Med") & (data["Lugage_boot"]=="Small") & ((data["Person"]=="4") | (data["Person"]=="More"))
  #
  print("Dataset dari cabang Person [2] : \n")
  print(data.loc[filter])
  print(
    "\nDikarenakan data dari cabang tersebut memiliki label homogen acc, \nmaka cabang tersebut dinyatakan sebagai leaf [acc]"
    )
  #
  print("\nDecision tree :")
  #
  #Struktur decision tree
  tree.iterasi7()

def iterasi8():
  import tree
  ###Iterasi Kedelapan###
  print("\n", "="*10,"Iterasi Kedelapan", "="*10, "\n")
  #
  filter = (data["Safety"]=="Med") & ((data["Lugage_boot"]=="Med") | (data["Person"]=="Big"))
  #
  print("Dataset dari cabang Person [2] : \n")
  print(data.loc[filter])
  print(
    "\nDikarenakan data dari cabang tersebut memiliki label homogen good, \nmaka cabang tersebut dinyatakan sebagai leaf [good]"
    )
  #
  print("\nDecision tree :")
  #
  #Struktur decision tree
  tree.iterasi8()
  
def iterasi9():
  from level2 import parent, impurity, median
  import tree
  ###Iterasi Kesembilan###
  print("\n", "="*10,"Iterasi Kesembilan", "="*10, "\n")
  #
  rule = (data['Safety'] == 'High')
  # rule
  #List/Array Gini atribut
  Buying =[impurity("Buying", "Low", 0, rule),impurity("Buying", "Med", "High", rule)]
  Maintenance = [impurity("Maintenance", "Low", 0, rule),impurity("Maintenance", "Med", "High", rule)]
  Doors = [impurity("Doors", "3", 0, rule),impurity("Doors", "4", "More", rule)]
  Person = [impurity("Person", "2", 0, rule),impurity("Person", "4", "More", rule)]
  Lugage_boot = [impurity("Lugage_boot", "Small", 0, rule),impurity("Lugage_boot", "Med", "Big", rule)]
  # Safety = [impurity("Safety", "Med", 0, rule),impurity("Safety", "High", 0, rule)]
  #
  parent = parent(rule)
  #
  median = [
            median(Buying, "Buying", "Low", "Med", "High", rule),median(Maintenance, "Maintenance", "Low", "Med", "High", rule),
            median(Doors, "Doors", "3", "4", "More", rule),median(Person, "Person", "2", "4", "More", rule),
            median(Lugage_boot, "Lugage_boot", "Small", "Med", "Big", rule)
            ]
  #
  gain = [
          parent-median[0], parent-median[1], parent-median[2],
          parent-median[3], parent-median[4]
        ]
  #Mencetak Hasil Perhitungan Iterasi Kesembilan
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

    # "\n\nImpurity Safety \\ Med -->", Safety[0],
    # "\nImpurity Safety \\ High -->", Safety[1],
    # "\nMedian Gini Safety -->", median[5],
    # "\nGain Safety -->", gain[5],
    ###Catatan : Nilai yang tertera berbeda dengan yang ada di modul
    ###Dikarenakan, Pada cabang anak kiri pada modul, terhitung LowHigh
    ###Yang dimana tidak dapat dilakukan karena record low telah menjadi
    ###Parent dari cabang ini / sudah tereliminasi
    "\n\nGain terbesar :", columns[gain.index(max(gain))],
    
    "\n\Lugage akan dijadikan sebagai parent untuk node selanjutnya,"
    "\nDikarenakan impurity Lugage adalah yang paling besar diantara semua atribut"
    "\n\nDecision tree :"
    )
  #
  #Struktur decision tree
  tree.iterasi9()
  #

def iterasi10():
  import tree
  ###Iterasi Kesepuluh###
  print("\n", "="*10,"Iterasi Kesepuluh", "="*10, "\n")
  #
  filter = (data["Safety"]=="High") & (data["Lugage_boot"]=="Small")
  #
  print("Dataset dari cabang Person [2] : \n")
  print(data.loc[filter])
  print(
    "\nDikarenakan data dari cabang tersebut memiliki label homogen good, \nmaka cabang tersebut dinyatakan sebagai leaf [good]"
    )
  #
  print("\nDecision tree :")
  #
  #Struktur decision tree
  tree.iterasi10()

def iterasi11():
  import tree
  ###Iterasi Kesebelas###
  print("\n", "="*10,"Iterasi Kesepuluh", "="*10, "\n")
  #
  filter = (data["Safety"]=="High") & ((data["Lugage_boot"]=="Med") | (data["Lugage_boot"]=="Big"))
  #
  print("Dataset dari cabang Person [2] : \n")
  print(data.loc[filter])
  print(
    "\nDikarenakan data dari cabang tersebut memiliki label homogen vgood, \nmaka cabang tersebut dinyatakan sebagai leaf [vgood]"
    )
  #
  print("\nDecision tree :")
  #
  #Struktur decision tree
  tree.iterasi11()