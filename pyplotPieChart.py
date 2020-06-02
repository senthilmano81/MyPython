import matplotlib.pyplot as plt
sizes = [3,4,6,2]
expld = [0.1,0,0,0]
labels = ['clsA','clsB', 'clsC', 'clsD']
colrs = ['red','blue','yellow','pink']
plt.pie(sizes,colors=colrs,labels=labels,autopct='%.1f%%',explode=expld)

plt.title("Pie Sample")
plt.axis("equal")
# to make circular pie char plt.axis("equal") should be used 
# plt.axis("equal")
plt.show()