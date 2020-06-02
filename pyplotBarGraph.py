import matplotlib.pyplot as plt

year = ['year-2012','year-2013','year-2014','year-2015', 'year-2016', 'year-2017']
salary = [12,13,14,17,19,20]
population = [100,120,180,250,300,370]


plt.bar(year,population,edgecolor='red',width=0.6)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Bar Graph Demo")
plt.xticks(rotation=40)
plt.show()