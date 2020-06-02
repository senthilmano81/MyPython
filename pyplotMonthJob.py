import matplotlib.pyplot as plt
import pandas as pd 
jobs = pd.read_csv('amazon_jobs_dataset.csv')
df = jobs.copy()
months = []
for date in df.Posting_date: 
    Month = date.split(',')[0].split()[0]
    months.append(Month)

df['Month'] = months
job_month = df.Month.value_counts()
months     = job_month.keys().tolist()
jobs      = job_month.tolist()
plt.bar(months,jobs,width=0.6,edgecolor='black')
plt.xticks(rotation=40)
plt.xlabel('Month')
plt.ylabel('Jobs')
plt.title('Jobs vs Month')
plt.grid()
plt.show()
for month in job_month.keys(): 
    print(month, job_month[month])