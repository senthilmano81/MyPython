import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('amazon_jobs_dataset.csv')
year = data['Posting_date'].str.split(', ',expand=True)[1]
basic_qualification=data['BASIC QUALIFICATIONS']
array=np.array(list(zip(year,basic_qualification)))
for i in range(len(array)): 
    if 'Java' in array[i][1] or 'java' in array[i][1]:
        array[i][1] = 1 
    else: 
        array[i][1] = 0
array = array[array[:,1]=='1']
array = array[:,0]
year=np.unique(array)
job=[]
for i in year: 
    job.append(len(array[array==i]))
plt.scatter(year,job,edgecolor='black',s=100)
plt.grid()
plt.show()
for i in range(len(year)): 
    print(year[i],job[i])