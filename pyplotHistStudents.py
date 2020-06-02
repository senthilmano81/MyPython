import matplotlib.pyplot as plt 
import numpy as np 
height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
## Weight
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]

heightmin = int(min(height))
heightmax = int(max(height))
hdelta = (heightmax - heightmin) /5 
print(hdelta)
print(heightmin)
print(heightmax)
a = [x for x in range(heightmin,heightmax,int(hdelta))]
print(a)


weightmin = float(min(weight))
weightmax = float(max(weight))
wdelta = (weightmax - weightmin) /5 
print(wdelta)
print(weightmin)
print(weightmax)
a = np.arange(weightmin,weightmax,wdelta)
a

plt.hist(height,bins=5,edgecolor='black')
plt.grid()
plt.show()



plt.hist(weight,bins=5,edgecolor='black')
plt.grid()
plt.show()
