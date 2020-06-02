import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
#gov_df.Killed.fillna(0,inplace=True)
#gov_df.Wounded.fillna(0,inplace=True)
red_states = ['Jharkhand', 'Odisha', 'Andhra Pradesh', 'Chhattisgarh']
df['Casualty'] = df.Killed + df.Wounded
years = df.Year.max() - df.Year.min() + 1
kashmir_count = df[(df.Country=='India') & (df.State == 'Jammu and Kashmir')].Casualty.sum()
kashmir_freq = kashmir_count / years
red_count = df[(df.Country=='India') & (df.State.isin(red_states))].Casualty.sum()
red_freq   = red_count / years
print(int(round(red_freq)), int(round(kashmir_freq)))