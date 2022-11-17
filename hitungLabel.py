def hitungLabel(arrayName):
  global a, b, c, d 
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