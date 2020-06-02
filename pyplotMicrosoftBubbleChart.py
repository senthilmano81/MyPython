import matplotlib.pyplot as plt
# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]

colors = range(len(year))
plt.scatter(year,revenue,s=employees,c=colors)
plt.title('Microsoft Statistics')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.grid()
plt.show()