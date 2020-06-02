import matplotlib.pyplot as plt
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
plt.axis("equal")
plt.pie(sold,labels=company,autopct='%.1f')
plt.show()
total = sum(sold)
for i in range(len(sold)): 
    print(company[i],'%.1f'%(sold[i]/total*100))
    