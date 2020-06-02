import matplotlib.pyplot as plt
import pandas as pd 

def substr(string): 
    return string[0:2]

def getCity(location): 
    loc = location.split(',')
    return loc[-1]

jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
df['Country'] = df.location.apply(substr)
ind_df = df[(df.Country=='IN')]
del ind_df['Country']
ind_df['City'] = ind_df.location.apply(getCity)
job_city = ind_df.City.value_counts()
plt.pie(job_city,labels=job_city.keys(),autopct='%.2f%%')
plt.axis("equal")
plt.show()

total_jobs = job_city.sum()
for city in job_city.keys(): 
    curpct = (job_city[city] / total_jobs)*100
    print(city,'%.2f%%'%(curpct))    
    
