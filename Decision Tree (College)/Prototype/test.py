import pandas as pd
import hitungLabel

df = pd.read_csv("Prototype\dbsample.csv")
filt = (df['Lugage_boot'] == 'Med') | (df['Lugage_boot'] == 'Big')

saringan = df.loc[filt, "Evaluation"].tolist()
hitungLabel.hitungLabel(saringan, 0)

unacc, acc, good, vgood = hitungLabel.a, hitungLabel.b, hitungLabel.c, hitungLabel.d
total = hitungLabel.total
giniDex = 1 - (unacc/total)**2 - (acc/total)**2 - (good/total)**2 - (vgood/total)**2

print(giniDex)