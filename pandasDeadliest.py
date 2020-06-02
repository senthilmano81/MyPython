import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
ind = df.Killed.idxmax()
print(df.Country[ind], int(df.Killed[ind]), df.Group[ind])

