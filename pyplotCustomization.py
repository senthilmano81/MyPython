import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
y1 = x**3
y2 = x**2

plt.plot(x,y1,color='black',marker='o', linewidth=1.5,label='X^3')
# alpha = 1 denotes completely opaque, alpha closer to zero is much more transparent 
plt.plot(x,y2,color='red',marker='p',linewidth=1.5,label='X^2',alpha=0.5)
plt.ylabel('Y')
plt.xlabel('X')
#plt.axis([0,10,0,200])
plt.grid()
plt.text(2,80,'Test',fontsize=12)
plt.title('Pyplot Demo')
plt.legend()
plt.show()