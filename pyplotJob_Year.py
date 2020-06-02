import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
years = []
for date in df.Posting_date: 
    years.append(date[-4:])
df['Year'] = years
job_year = df.Year.value_counts().sort_index()
years     = job_year.keys().tolist()
jobs      = job_year.tolist()
plt.plot(years,jobs)
plt.xlabel('Year')
plt.ylabel('Jobs')
plt.title('Jobs Vs Year')
plt.show()
for year in job_year.keys(): 
    print(year, job_year[year])