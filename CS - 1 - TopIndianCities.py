# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getCity(location): 
    location = str(location)
    if '/' in location: 
        loc = location.split('/')
        location = loc[0]
    
    if location.title() == 'Delhi': 
        city = 'New Delhi'
    else: 
        city = location
    return city.strip().title()

def str2int(string): 
    return int(string.replace(',',''))

data = pd.read_csv('startup_funding.csv')
df   = data.copy()
df['City'] = df.CityLocation.apply(getCity)
df.AmountInUSD.fillna("0",inplace=True)
df['AmountInUSD'] = df.AmountInUSD.apply(str2int)
groupcols = df.groupby(['City'])['AmountInUSD'].sum()
groupcols = groupcols.sort_values()

cities = []
fund   = []
for i in range(len(groupcols)-1,len(groupcols)-1-11,-1): 
    if groupcols.keys()[i] == 'Nan': 
        continue 
    cities.append(groupcols.keys()[i])
    fund.append(groupcols[i])
    
total = sum(fund)
for i in range(len(cities)): 
    print(cities[i],'%.2f'%(fund[i]/total*100))