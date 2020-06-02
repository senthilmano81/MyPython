## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np 
import csv
with open('terrorismData.csv') as file_obj: 
    file_data = csv.DictReader(file_obj,skipinitialspace=True)
    
    killed = []
    country = []
    for row in file_data: 
        killed.append(row['Killed'])
        country.append(row['Country'])
    
    np_killed = np.array(killed)
    np_country = np.array(country)
    
    np_killed[np_killed == ''] = '0.0'
    np_killed = np.array(np_killed,dtype=float)
    np_killed = np.array(np_killed,dtype=int)
    bool_arr = [np_country == 'United States']
    np_killed_USA = np_killed[bool_arr]
    for kill_cnt in np_killed_USA: 
        print(kill_cnt)
   