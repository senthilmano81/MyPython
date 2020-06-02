import pandas as pd
cols =['SL','SW','PL','PW','Species']
iris = pd.read_csv("iris.data",names=cols)
df = iris.copy()

iris_v_df= df[(df['Species'] == 'Iris-virginica') & (df['PW'] > 1.5)]
print(iris_v_df)
print(iris_v_df.index)
for i in iris_v_df.index:
    print(iris_v_df.loc[i, 'SL'], iris_v_df.loc[i, 'SW'], iris_v_df.loc[i, 'PL'], iris_v_df.loc[i, 'PW'], iris_v_df.loc[i, 'Species'])


a= 'Senthil' 
b = ' Manoharan'
c = a + b
print(c)