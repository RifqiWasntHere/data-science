import pandas as pd
def cariData(arrayName):
                                                    


  for i in range(len(arrayName)):
    if ( arrayName[i] == "unacc" ):
      unacc += 1
    elif ( arrayName[i] == "acc" ):
      acc += 1
    elif ( arrayName[i] == "good" ):
      good += 1
    elif ( arrayName[i] == "vgood" ):
      vgood += 1

  print( "str(arrayName" )