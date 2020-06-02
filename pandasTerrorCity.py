import pandas as pd
terData = pd.read_csv('terrorismData.csv')
df = terData.copy()
new_df = df[(df['State'] == 'Jammu and Kashmir')] 
city_group = new_df['City'].value_counts()
city_name  = city_group.keys()[0]
city_attacks = city_group[0]

city_df = new_df[(new_df.City==city_name) & (new_df.Group != 'Unknown')]
grp_group  = city_df['Group'].value_counts()
print(city_name, city_attacks,grp_group.keys()[0])