import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = df.Posting_date.str.split(',',expand=True).iloc[:,1]
arr   = (df['BASIC QUALIFICATIONS'].str.find('Java') >= 0 )  | (df['BASIC QUALIFICATIONS'].str.find('java') >= 0 ) 
valid_years = years[arr]
java_years = valid_years.value_counts().sort_index()
plt.scatter(java_years.keys().tolist(),java_years.tolist(),edgecolor='black',s=100)
plt.grid()
plt.show()
for year in java_years.keys(): 
    print(year,java_years[year])