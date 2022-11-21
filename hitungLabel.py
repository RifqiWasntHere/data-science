def hitungLabel(arrayName, arrayName2):
  global a, b, c, d, total
  a, b, c, d = 0, 0, 0, 0
  for i in range(len(arrayName)):
    if ( arrayName[i] == "unacc" ):
      a += 1
    elif ( arrayName[i] == "acc" ):
      b += 1
    elif ( arrayName[i] == "good" ):
      c += 1
    elif ( arrayName[i] == "vgood" ):
      d += 1


  for i in range(len(arrayName2)):
    if ( arrayName2[i] == "unacc" ):
      a += 1
    elif ( arrayName2[i] == "acc" ):
      b += 1
    elif ( arrayName2[i] == "good" ):
      c += 1
    elif ( arrayName2[i] == "vgood" ):
      d += 1
  total = a + b + c + d
  
