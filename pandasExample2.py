import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv('iris.data',names=cols)
df = iris.copy()
print(df.SL.mean())




gender = ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F']
a = [1,2,3,4,5,6]
sum(gender,key=lambda g:1 if (g=='M') else 0)
    
    