# Open and read data file as specified in the question
# Print the required output in given format
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

def getYear(String): 
    return String[-4:]

data = pd.read_csv('startup_funding.csv')
df   = data.copy()
year = df.Date.apply(getYear)

fund_year = year.value_counts().sort_index()
plt.plot(fund_year.keys(),fund_year)
plt.grid()
plt.xlabel('Year')
plt.ylabel('Fund')
plt.title('Fundings per year')

for year in fund_year.keys(): 
    print(year,fund_year[year])