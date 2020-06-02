import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
location = data['location'].str.split(', ',expand=True)
arr = location[0] == 'IN'
india_city = location[arr][2]
freq = india_city.value_counts()
plt.axis('equal')
x = freq.index
plt.pie(freq,labels=x,autopct='%.2f%%')
plt.show()
perc = np.true_divide(freq,freq.sum(axis=0))*100
for i in range(len(x)):
    print(x[i],format(perc[i],'.2f'))
